import logging
from datetime import timedelta, datetime

from celery import shared_task
from django.conf import settings

from accounts.models import Account
from connectors.crud.connectors_crud import get_db_connector_keys, get_db_connectors

from executor.crud.playbook_execution_crud import create_playbook_execution, get_db_playbook_execution
from executor.crud.playbooks_crud import get_db_playbooks
from executor.playbook_source_facade import playbook_source_facade
from executor.tasks import execute_playbook
from executor.workflows.action.action_executor import action_executor
from executor.workflows.crud.workflow_execution_crud import get_db_workflow_executions, \
    update_db_account_workflow_execution_status, \
    get_db_workflow_execution_logs, get_workflow_executions, create_workflow_execution_log, \
    update_db_account_workflow_execution_count_increment
from executor.workflows.crud.workflows_crud import get_db_workflows
from executor.source_processors.slack_api_processor import SlackApiProcessor
from intelligence_layer.result_interpreters.result_interpreter_facade import playbook_step_execution_result_interpret
from management.crud.task_crud import get_or_create_task
from management.models import TaskRun, PeriodicTaskStatus
from management.utils.celery_task_signal_utils import publish_pre_run_task, publish_task_failure, publish_post_run_task
from protos.playbooks.playbook_pb2 import PlaybookTaskExecutionLog as PlaybookTaskExecutionLogProto, \
    PlaybookStepExecutionLog as PlaybookStepExecutionLogProto
from utils.time_utils import current_datetime, current_epoch_timestamp
from protos.base_pb2 import TimeRange, SourceKeyType
from protos.playbooks.intelligence_layer.interpreter_pb2 import Interpretation as InterpretationProto
from protos.playbooks.deprecated_playbook_pb2 import DeprecatedPlaybookExecution
from protos.playbooks.workflow_pb2 import WorkflowExecutionStatusType, Workflow as WorkflowProto, \
    WorkflowAction as WorkflowActionProto, WorkflowActionSlackNotificationConfig
from protos.base_pb2 import Source

from utils.proto_utils import dict_to_proto, proto_to_dict

logger = logging.getLogger(__name__)


@shared_task(max_retries=3, default_retry_delay=10)
def workflow_scheduler():
    current_time_utc = current_datetime()
    current_time = int(current_time_utc.timestamp())
    all_scheduled_wf_executions = get_workflow_executions(
        status_in=[WorkflowExecutionStatusType.WORKFLOW_SCHEDULED, WorkflowExecutionStatusType.WORKFLOW_RUNNING])
    for wf_execution in all_scheduled_wf_executions:
        workflow_id = wf_execution.workflow_id
        logger.info(f"Scheduling workflow execution:: workflow_execution_id: {wf_execution.id}, workflow_id: "
                    f"{workflow_id} at {current_time}")
        account = wf_execution.account
        time_range = wf_execution.time_range
        update_time_range = None
        if wf_execution.status == WorkflowExecutionStatusType.WORKFLOW_CANCELLED:
            logger.info(f"Workflow execution cancelled for workflow_execution_id: {wf_execution.id}, workflow_id: "
                        f"{workflow_id} at {current_time}")
            continue

        scheduled_at = wf_execution.scheduled_at
        if current_time_utc < scheduled_at:
            logger.info(f"Workflow execution not scheduled yet for workflow_execution_id: {wf_execution.id}, "
                        f"workflow_id: {workflow_id} at {current_time}")
            continue

        expiry_at = wf_execution.expiry_at
        interval = wf_execution.interval
        if current_time_utc > expiry_at + timedelta(seconds=int(settings.WORKFLOW_SCHEDULER_INTERVAL)):
            logger.info(f"Workflow execution expired for workflow_execution_id: {wf_execution.id}, workflow_id: "
                        f"{workflow_id} at {current_time}")
            update_db_account_workflow_execution_status(account, wf_execution.id, scheduled_at,
                                                        WorkflowExecutionStatusType.WORKFLOW_FINISHED)
            continue
        if interval:
            next_schedule = current_time_utc
            wf_execution_logs = get_db_workflow_execution_logs(account, wf_execution.id)
            if wf_execution_logs.exists():
                latest_wf_execution_log = wf_execution_logs.first()
                next_schedule = latest_wf_execution_log.created_at + timedelta(seconds=interval)
            if current_time_utc < next_schedule:
                logger.info(f"Next Workflow execution interval not reached for workflow_execution_id: "
                            f"{wf_execution.id}, workflow_id: {workflow_id} at {current_time}")
                continue
            else:
                update_time_range = {'time_geq': int(next_schedule.timestamp()) - 3600,
                                     'time_lt': int(next_schedule.timestamp())}

        update_db_account_workflow_execution_count_increment(account, wf_execution.id)
        if wf_execution.status == WorkflowExecutionStatusType.WORKFLOW_SCHEDULED:
            update_db_account_workflow_execution_status(account, wf_execution.id, scheduled_at,
                                                        WorkflowExecutionStatusType.WORKFLOW_RUNNING)
        all_pbs = wf_execution.workflow.playbooks.filter(workflowplaybookmapping__is_active=True)
        all_playbook_ids = [pb.id for pb in all_pbs]
        for pb_id in all_playbook_ids:
            try:
                playbook_run_uuid = f'{str(current_time)}_{account.id}_{pb_id}_pb_run'
                if update_time_range:
                    time_range_proto = dict_to_proto(update_time_range, TimeRange)
                else:
                    time_range_proto = dict_to_proto(time_range, TimeRange)
                playbook_execution = create_playbook_execution(account, time_range_proto, pb_id, playbook_run_uuid,
                                                               wf_execution.created_by)
                saved_task = get_or_create_task(workflow_executor.__name__, account.id, workflow_id, wf_execution.id,
                                                pb_id, playbook_execution.id, time_range)
                if not saved_task:
                    logger.error(f"Failed to create workflow execution task for account: {account.id}, workflow_id: "
                                 f"{workflow_id}, workflow_execution_id: {wf_execution.id}, playbook_id: {pb_id}")
                    continue
                task = workflow_executor.delay(account.id, workflow_id, wf_execution.id, pb_id, playbook_execution.id,
                                               time_range)
                task_run = TaskRun.objects.create(task=saved_task, task_uuid=task.id,
                                                  status=PeriodicTaskStatus.SCHEDULED,
                                                  account_id=account.id,
                                                  scheduled_at=datetime.fromtimestamp(float(current_time)))
            except Exception as e:
                logger.error(f"Failed to create playbook execution:: workflow_id: {workflow_id}, workflow_execution_id:"
                             f" {wf_execution.id} playbook_id: {pb_id}, error: {e}")
                update_db_account_workflow_execution_status(account, wf_execution.id, scheduled_at,
                                                            WorkflowExecutionStatusType.WORKFLOW_FAILED)
                continue
        if not interval:
            logger.info(f"Workflow execution interval not set for workflow_execution_id, "
                        f"marking complete: {wf_execution.id}")
            update_db_account_workflow_execution_status(account, wf_execution.id, scheduled_at,
                                                        WorkflowExecutionStatusType.WORKFLOW_FINISHED)
            continue


workflow_scheduler_prerun_notifier = publish_pre_run_task(workflow_scheduler)
workflow_scheduler_failure_notifier = publish_task_failure(workflow_scheduler)
workflow_scheduler_postrun_notifier = publish_post_run_task(workflow_scheduler)


@shared_task(max_retries=3, default_retry_delay=10)
def workflow_executor(account_id, workflow_id, workflow_execution_id, playbook_id, playbook_execution_id, time_range):
    current_time = current_datetime().timestamp()
    logger.info(f"Running workflow execution:: account_id: {account_id}, workflow_execution_id: "
                f"{workflow_execution_id}, playbook_execution_id: {playbook_execution_id}")
    try:
        create_workflow_execution_log(account_id, workflow_id, workflow_execution_id, playbook_execution_id)
        execute_playbook(account_id, playbook_id, playbook_execution_id, time_range)
        try:
            saved_task = get_or_create_task(workflow_action_execution.__name__, account_id, workflow_id,
                                            workflow_execution_id, playbook_execution_id)
            if not saved_task:
                logger.error(f"Failed to create workflow action execution task for account: {account_id}, workflow_id: "
                             f"{workflow_id}, workflow_execution_id: {workflow_execution_id}, playbook_id: "
                             f"{playbook_id}")
                return
            task = workflow_action_execution.delay(account_id, workflow_id, workflow_execution_id,
                                                   playbook_execution_id)
            task_run = TaskRun.objects.create(task=saved_task, task_uuid=task.id,
                                              status=PeriodicTaskStatus.SCHEDULED,
                                              account_id=account_id,
                                              scheduled_at=datetime.fromtimestamp(float(current_time)))
        except Exception as e:
            logger.error(
                f"Failed to create workflow action execution:: workflow_id: {workflow_id}, workflow_execution_id: "
                f"{workflow_execution_id} playbook_id: {playbook_id}, error: {e}")
    except Exception as exc:
        logger.error(f"Error occurred while running workflow execution: {exc}")
        raise exc


workflow_executor_prerun_notifier = publish_pre_run_task(workflow_executor)
workflow_executor_failure_notifier = publish_task_failure(workflow_executor)
workflow_executor_postrun_notifier = publish_post_run_task(workflow_executor)


@shared_task(max_retries=3, default_retry_delay=10)
def workflow_action_execution(account_id, workflow_id, workflow_execution_id, playbook_execution_id):
    logger.info(f"Running workflow action execution:: account_id: {account_id}, workflow_execution_id: "
                f"{workflow_execution_id}, playbook_execution_id: {playbook_execution_id}")
    account = Account.objects.get(id=account_id)
    try:
        workflows = get_db_workflows(account, workflow_id=workflow_id)
        workflow_executions = get_db_workflow_executions(account, workflow_execution_id)
        playbook_executions = get_db_playbook_execution(account, playbook_execution_id=playbook_execution_id)
        if not workflows:
            logger.error(f"Aborting workflow action execution as workflow not found for "
                         f"account_id: {account_id}, workflow_id: {workflow_id}")
        if not workflow_executions:
            logger.error(f"Aborting workflow action execution as workflow execution not found for "
                         f"account_id: {account_id}, workflow_execution_id: {workflow_execution_id}")
        if not playbook_executions:
            logger.error(f"Aborting workflow action execution as playbook execution not found for "
                         f"account_id: {account_id}, playbook_execution_id: {playbook_execution_id}")
        thread_ts = None
        workflow_execution = workflow_executions.first()
        if workflow_execution.metadata:
            thread_ts = workflow_execution.metadata.get('thread_ts', None)

        playbook_execution = playbook_executions.first()
        pe_proto: DeprecatedPlaybookExecution = playbook_execution.proto
        p_proto = pe_proto.playbook
        step_execution_logs = pe_proto.step_execution_logs
        execution_output: [InterpretationProto] = playbook_step_execution_result_interpret(p_proto,
                                                                                           step_execution_logs)
        workflow = workflows.first()
        w_proto: WorkflowProto = workflow.proto
        w_actions = w_proto.actions
        for w_action in w_actions:
            if w_action.type == WorkflowActionProto.Type.NOTIFY:
                w_action_dict = proto_to_dict(w_action)
                if w_action_dict.get('notification_config', {}).get('slack_config', {}).get('message_type',
                                                                                            None) == 'THREAD_REPLY' and thread_ts:
                    w_action_dict['notification_config']['slack_config']['thread_ts'] = thread_ts
                    updated_w_action = dict_to_proto(w_action_dict, WorkflowActionProto)
                    action_executor(account, updated_w_action, execution_output)
                else:
                    action_executor(account, w_action, execution_output)
            else:
                action_executor(account, w_action, execution_output)
    except Exception as exc:
        logger.error(f"Error occurred while running workflow action execution: {exc}")
        raise exc


workflow_action_execution_prerun_notifier = publish_pre_run_task(workflow_action_execution)
workflow_action_execution_failure_notifier = publish_task_failure(workflow_action_execution)
workflow_action_execution_postrun_notifier = publish_post_run_task(workflow_action_execution)


def test_workflow_notification(account_id, workflow, message_type):
    try:
        account = Account.objects.get(id=account_id)
    except Exception as e:
        logger.error(f"Account not found for account_id: {account_id}, error: {e}")
        return
    current_time_epoch = current_epoch_timestamp()
    tr = TimeRange(time_lt=current_time_epoch, time_geq=current_time_epoch - 3600)
    playbook_id = workflow.playbooks[0].id.value
    playbooks = get_db_playbooks(account, playbook_id=playbook_id)
    if not playbooks:
        logger.error(f"Playbook not found for account_id: {account_id}, playbook_id: {playbook_id}")
        return
    playbook = playbooks.first()
    pb_proto = playbook.proto
    playbook_steps = pb_proto.steps
    if message_type == WorkflowActionSlackNotificationConfig.MessageType.THREAD_REPLY:
        logger.info("Sending test thread reply message")
        channel_id = workflow.entry_points[0].alert_config.slack_channel_alert_config.slack_channel_id.value
        slack_connectors = get_db_connectors(account, connector_type=Source.SLACK, is_active=True)
        if not slack_connectors:
            logger.error(f"Active Slack connector not found for account_id: {account_id}")
            return

        slack_connector = slack_connectors.first()
        bot_auth_token_slack_connector_keys = get_db_connector_keys(account, slack_connector.id,
                                                                    key_type=SourceKeyType.SLACK_BOT_AUTH_TOKEN)
        if not bot_auth_token_slack_connector_keys:
            logger.error(f"Bot auth token not found for account_id: {account_id}")
            return

        bot_auth_token = bot_auth_token_slack_connector_keys.first().key
        message_ts = SlackApiProcessor(bot_auth_token).send_bot_message(channel_id,
                                                                        'Hello, this is a test alert message from the Playbooks Slack Droid to show how the enrichment works in reply to an alert.')
        workflow.actions[0].notification_config.slack_config.thread_ts.value = message_ts
    elif message_type == WorkflowActionSlackNotificationConfig.MessageType.MESSAGE:
        logger.info("Sending test message")
    else:
        logger.error(f"Invalid message type: {message_type}")
        return
    step_execution_logs: [PlaybookStepExecutionLogProto] = []
    try:
        global_variable_set = pb_proto.global_variable_set
        for step in playbook_steps:
            tasks = step.tasks
            pe_logs = []
            for task_proto in tasks:
                task_result = playbook_source_facade.execute_task(account.id, tr, global_variable_set, task_proto)
                playbook_execution_log = PlaybookTaskExecutionLogProto(task=task_proto, result=task_result)
                pe_logs.append(playbook_execution_log)
            step_execution_log = PlaybookStepExecutionLogProto(step=step, task_execution_logs=pe_logs)
            step_execution_logs.append(step_execution_log)
    except Exception as exc:
        logger.error(f"Error occurred while running playbook: {exc}")

    execution_output: [InterpretationProto] = playbook_step_execution_result_interpret(pb_proto,
                                                                                       step_execution_logs)
    action_executor(account, workflow.actions[0], execution_output)
