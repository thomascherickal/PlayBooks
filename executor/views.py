import logging
import os
import json
from typing import Union

from django.conf import settings
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from google.protobuf.wrappers_pb2 import BoolValue, StringValue
from rest_framework.decorators import api_view
from google.protobuf.struct_pb2 import Struct

from accounts.models import Account, get_request_account, get_request_user, get_api_token_user
from connectors.crud.connectors_crud import get_db_account_connectors
from executor.crud.playbook_execution_crud import create_playbook_execution, get_db_playbook_execution, \
    update_db_account_playbook_execution_status, bulk_create_playbook_execution_log
from executor.crud.deprecated_playbooks_crud import deprecated_update_or_create_db_playbook
from executor.crud.deprecated_playbooks_update_processor import deprecated_playbooks_update_processor
from executor.crud.playbooks_update_processor import playbooks_update_processor
from executor.crud.playbooks_crud import update_or_create_db_playbook
from executor.deprecated_task_executor import deprecated_execute_task
from executor.playbook_source_facade import playbook_source_facade
from executor.tasks import execute_playbook, execute_playbook_impl, store_step_execution_logs
from executor.utils.old_to_new_model_transformers import transform_PlaybookTaskExecutionResult_to_PlaybookTaskResult
from intelligence_layer.result_interpreters.result_interpreter_facade import task_result_interpret, \
    step_result_interpret
from management.crud.task_crud import get_or_create_task, check_scheduled_or_running_task_run_for_task
from management.models import TaskRun, PeriodicTaskStatus
from playbooks.utils.decorators import web_api, account_post_api, account_get_api, get_proto_schema_validator, \
    deprecated
from playbooks.utils.meta import get_meta
from playbooks.utils.queryset import filter_page
from protos.base_pb2 import Source as ConnectorType
from protos.playbooks.intelligence_layer.interpreter_pb2 import InterpreterType, Interpretation as InterpretationProto
from protos.playbooks.playbook_commons_pb2 import PlaybookTaskResult, PlaybookExecutionStatusType
from protos.playbooks.playbook_pb2 import PlaybookTask, PlaybookTaskExecutionLog, PlaybookStepExecutionLog, \
    PlaybookExecution, Playbook
from utils.time_utils import current_epoch_timestamp, current_datetime
from protos.base_pb2 import Meta, TimeRange, Message, Page
from protos.playbooks.api_pb2 import RunPlaybookTaskRequest, RunPlaybookTaskResponse, RunPlaybookStepRequest, \
    RunPlaybookStepResponse, CreatePlaybookRequest, CreatePlaybookResponse, GetPlaybooksRequest, GetPlaybooksResponse, \
    UpdatePlaybookRequest, UpdatePlaybookResponse, ExecutePlaybookRequest, ExecutePlaybookResponse, \
    ExecutionPlaybookGetRequest, ExecutionPlaybookGetResponse, ExecutionsPlaybooksListResponse, \
    ExecutionsPlaybooksListRequest, ExecutionPlaybookAPIGetResponse, PlaybookTemplatesGetResponse, \
    RunPlaybookTaskResponseV2, RunPlaybookStepResponseV2, RunPlaybookRequest, RunPlaybookResponse, \
    PlaybooksBuilderOptionsRequest, PlaybooksBuilderOptionsResponse, RunPlaybookTaskRequestV3, \
    RunPlaybookTaskResponseV3, GetPlaybooksRequestV2, GetPlaybooksResponseV2, RunPlaybookStepRequestV3, \
    RunPlaybookStepResponseV3, RunPlaybookRequestV2, RunPlaybookResponseV2, CreatePlaybookRequestV2, \
    CreatePlaybookResponseV2, UpdatePlaybookRequestV2, UpdatePlaybookResponseV2, ExecutionPlaybookGetRequestV2, \
    ExecutionPlaybookGetResponseV2, ExecutionPlaybookAPIGetResponseV2

from protos.playbooks.deprecated_playbook_pb2 import DeprecatedPlaybookTaskExecutionResult, DeprecatedPlaybook, \
    DeprecatedPlaybookExecutionLog, DeprecatedPlaybookStepExecutionLog, DeprecatedPlaybookExecution
from utils.proto_utils import proto_to_dict, dict_to_proto

logger = logging.getLogger(__name__)


@web_api(RunPlaybookTaskRequest)
@deprecated
def task_run(request_message: RunPlaybookTaskRequest) -> Union[RunPlaybookTaskResponse, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    task = request_message.playbook_task_definition
    try:
        task_execution_result = deprecated_execute_task(account.id, time_range, task)
    except Exception as e:
        return RunPlaybookTaskResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       task_execution_result=DeprecatedPlaybookTaskExecutionResult(
                                           error=StringValue(value=str(e))))
    return RunPlaybookTaskResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                   task_execution_result=task_execution_result)


@web_api(RunPlaybookTaskRequest)
@deprecated
def task_run_v2(request_message: RunPlaybookTaskRequest) -> Union[RunPlaybookTaskResponseV2, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))

    task = request_message.playbook_task_definition
    interpreter_type: InterpreterType = task.interpreter_type if task.interpreter_type else InterpreterType.BASIC_I
    try:
        task_execution_result = deprecated_execute_task(account.id, time_range, task)
        playbook_task_result = transform_PlaybookTaskExecutionResult_to_PlaybookTaskResult(task_execution_result)
        interpretation: InterpretationProto = task_result_interpret(interpreter_type, task, playbook_task_result)
    except Exception as e:
        playbook_execution_log = DeprecatedPlaybookExecutionLog(
            task=task,
            task_execution_result=DeprecatedPlaybookTaskExecutionResult(error=StringValue(value=str(e)))
        )
        return RunPlaybookTaskResponseV2(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                         task_execution_log=playbook_execution_log)
    playbook_execution_log = DeprecatedPlaybookExecutionLog(
        task=task,
        task_execution_result=task_execution_result,
        task_interpretation=interpretation
    )
    return RunPlaybookTaskResponseV2(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                     task_execution_log=playbook_execution_log)


@web_api(RunPlaybookTaskRequestV3)
def task_run_v3(request_message: RunPlaybookTaskRequestV3) -> Union[RunPlaybookTaskResponseV3, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))

    task: PlaybookTask = request_message.playbook_task
    global_variable_set = {}
    if request_message.global_variable_set:
        global_variable_set = proto_to_dict(request_message.global_variable_set)
    elif task.global_variable_set:
        global_variable_set = proto_to_dict(task.global_variable_set)
    interpreter_type: InterpreterType = task.interpreter_type if task.interpreter_type else InterpreterType.BASIC_I
    try:
        task_result = playbook_source_facade.execute_task(account.id, time_range, global_variable_set, task)
        interpretation: InterpretationProto = task_result_interpret(interpreter_type, task, task_result)
        playbook_task_execution_log = PlaybookTaskExecutionLog(task=task, result=task_result,
                                                               interpretation=interpretation)
    except Exception as e:
        playbook_task_execution_log = PlaybookTaskExecutionLog(task=task,
                                                               result=PlaybookTaskResult(
                                                                   error=StringValue(value=str(e))))
    return RunPlaybookTaskResponseV3(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                     playbook_task_execution_log=playbook_task_execution_log)


@web_api(RunPlaybookStepRequest)
@deprecated
def step_run(request_message: RunPlaybookStepRequest) -> Union[RunPlaybookStepResponse, HttpResponse]:
    account: Account = get_request_account()
    step = request_message.playbook_step
    tasks = step.tasks
    task_execution_results = []
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    for task in tasks:
        try:
            task_result = deprecated_execute_task(account.id, time_range, task)
            task_execution_results.append(task_result)
        except Exception as e:
            task_execution_results.append(DeprecatedPlaybookTaskExecutionResult(error=StringValue(value=str(e))))

    return RunPlaybookStepResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True), name=step.name,
                                   description=step.description, task_execution_results=task_execution_results)


@web_api(RunPlaybookStepRequest)
@deprecated
def step_run_v2(request_message: RunPlaybookStepRequest) -> Union[RunPlaybookStepResponseV2, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))

    step = request_message.playbook_step
    tasks = step.tasks
    interpreter_type: InterpreterType = step.interpreter_type if step.interpreter_type else InterpreterType.BASIC_I

    pe_logs = []
    task_interpretations = []
    for task in tasks:
        try:
            task_execution_result = deprecated_execute_task(account.id, time_range, task)
            new_task_result = transform_PlaybookTaskExecutionResult_to_PlaybookTaskResult(task_execution_result)
            interpretation: InterpretationProto = task_result_interpret(interpreter_type, task, new_task_result)
            playbook_execution_log = DeprecatedPlaybookExecutionLog(
                step=step,
                task=task,
                task_execution_result=task_execution_result,
                task_interpretation=interpretation
            )
            pe_logs.append(playbook_execution_log)
            task_interpretations.append(interpretation)
        except Exception as e:
            playbook_execution_log = DeprecatedPlaybookExecutionLog(
                task=task,
                task_execution_result=DeprecatedPlaybookTaskExecutionResult(error=StringValue(value=str(e)))
            )
            pe_logs.append(playbook_execution_log)

    step_interpretation: InterpretationProto = step_result_interpret(interpreter_type, step, task_interpretations)
    step_execution_log = DeprecatedPlaybookStepExecutionLog(step=step, logs=pe_logs,
                                                            step_interpretation=step_interpretation)

    return RunPlaybookStepResponseV2(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                     step_execution_log=step_execution_log)


@web_api(RunPlaybookStepRequestV3)
def step_run_v3(request_message: RunPlaybookStepRequestV3) -> Union[RunPlaybookStepResponseV3, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))

    step = request_message.playbook_step
    tasks = step.tasks
    interpreter_type: InterpreterType = step.interpreter_type if step.interpreter_type else InterpreterType.BASIC_I

    pte_logs = []
    task_interpretations = []
    for task in tasks:
        try:
            global_variable_set = {}
            if task.global_variable_set:
                global_variable_set = proto_to_dict(task.global_variable_set)
            task_result = playbook_source_facade.execute_task(account.id, time_range, global_variable_set, task)
            interpretation: InterpretationProto = task_result_interpret(interpreter_type, task, task_result)
            playbook_task_execution_log = PlaybookTaskExecutionLog(task=task, result=task_result,
                                                                   interpretation=interpretation)
            task_interpretations.append(interpretation)
        except Exception as e:
            playbook_task_execution_log = PlaybookTaskExecutionLog(task=task,
                                                                   result=PlaybookTaskResult(
                                                                       error=StringValue(value=str(e))))
        pte_logs.append(playbook_task_execution_log)

    step_interpretation: InterpretationProto = step_result_interpret(interpreter_type, step, task_interpretations)
    step_execution_log = PlaybookStepExecutionLog(step=step, task_execution_logs=pte_logs,
                                                  step_interpretation=step_interpretation)

    return RunPlaybookStepResponseV3(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                     step_execution_log=step_execution_log)


@web_api(RunPlaybookRequest)
@deprecated
def playbook_run(request_message: RunPlaybookRequest) -> Union[RunPlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))

    playbook = request_message.playbook
    steps = playbook.steps
    step_execution_logs = []
    for step in steps:
        tasks = step.tasks
        interpreter_type: InterpreterType = step.interpreter_type if step.interpreter_type else InterpreterType.BASIC_I
        pe_logs = []
        task_interpretations = []
        for task in tasks:
            try:
                task_execution_result = deprecated_execute_task(account.id, time_range, task)
                playbook_task_result = transform_PlaybookTaskExecutionResult_to_PlaybookTaskResult(
                    task_execution_result)
                interpretation: InterpretationProto = task_result_interpret(interpreter_type, task,
                                                                            playbook_task_result)
                playbook_execution_log = DeprecatedPlaybookExecutionLog(
                    step=step,
                    task=task,
                    task_execution_result=task_execution_result,
                    task_interpretation=interpretation
                )
                pe_logs.append(playbook_execution_log)
                task_interpretations.append(interpretation)
            except Exception as e:
                playbook_execution_log = DeprecatedPlaybookExecutionLog(
                    task=task,
                    task_execution_result=DeprecatedPlaybookTaskExecutionResult(error=StringValue(value=str(e)))
                )
                pe_logs.append(playbook_execution_log)

        step_interpretations: InterpretationProto = step_result_interpret(interpreter_type, step,
                                                                          task_interpretations)
        step_execution_log = DeprecatedPlaybookStepExecutionLog(step=step, logs=pe_logs,
                                                                step_interpretation=step_interpretations)
        step_execution_logs.append(step_execution_log)
    playbook_execution = DeprecatedPlaybookExecution(playbook=playbook, time_range=time_range,
                                                     step_execution_logs=step_execution_logs)
    return RunPlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                               playbook_execution=playbook_execution)


@web_api(RunPlaybookRequestV2)
def playbook_run_v2(request_message: RunPlaybookRequestV2) -> Union[RunPlaybookResponseV2, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    current_time = current_epoch_timestamp()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    playbook: Playbook = request_message.playbook

    db_playbook = None
    db_playbook_execution = None
    if playbook.id and playbook.id.value:
        playbook_run_uuid = f'{str(current_time)}_{account.id}_{playbook.id.value}_pb_run'
        try:
            db_playbook = account.playbook_set.get(id=playbook.id.value, is_active=True)
            db_playbook_execution = create_playbook_execution(account, time_range, playbook.id.value, playbook_run_uuid,
                                                              user.email)
        except Exception as e:
            logger.error(e)

    try:
        step_execution_logs = execute_playbook_impl(time_range, account, playbook)
        playbook_execution = PlaybookExecution(playbook=playbook, time_range=time_range,
                                               step_execution_logs=step_execution_logs)
        if db_playbook and db_playbook_execution:
            store_step_execution_logs(account, db_playbook, db_playbook_execution, step_execution_logs)
            update_db_account_playbook_execution_status(account, db_playbook_execution.id,
                                                        PlaybookExecutionStatusType.FINISHED)
        return RunPlaybookResponseV2(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                     playbook_execution=playbook_execution)
    except Exception as e:
        logger.error(f"Error running playbook: {e}")
        if db_playbook_execution:
            update_db_account_playbook_execution_status(account, db_playbook_execution.id,
                                                        PlaybookExecutionStatusType.FAILED)
        return RunPlaybookResponseV2(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                     message=Message(title="Error", description=str(e)))


@web_api(GetPlaybooksRequest)
@deprecated
def playbooks_get(request_message: GetPlaybooksRequest) -> Union[GetPlaybooksResponse, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    show_inactive = meta.show_inactive
    page: Page = meta.page
    list_all = True

    qs: QuerySet = account.playbook_set.all()
    if request_message.playbook_ids:
        qs = qs.filter(id__in=request_message.playbook_ids)
        list_all = False
    elif not show_inactive or not show_inactive.value:
        qs = qs.filter(is_active=True)

    total_count = qs.count()
    qs = qs.order_by('-created_at')
    qs = filter_page(qs, page)

    playbooks_list = list(pb.deprecated_proto_partial for pb in qs)
    if not list_all:
        playbooks_list = list(pb.deprecated_proto for pb in qs)
    return GetPlaybooksResponse(meta=get_meta(page=page, total_count=total_count), playbooks=playbooks_list)


@web_api(GetPlaybooksRequestV2)
def playbooks_get_v2(request_message: GetPlaybooksRequestV2) -> Union[GetPlaybooksResponseV2, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    show_inactive = meta.show_inactive
    page: Page = meta.page
    list_all = True

    qs: QuerySet = account.playbook_set.all()
    if request_message.playbook_ids:
        qs = qs.filter(id__in=request_message.playbook_ids)
        list_all = False
    elif not show_inactive or not show_inactive.value:
        qs = qs.filter(is_active=True)

    total_count = qs.count()
    qs = qs.order_by('-created_at')
    qs = filter_page(qs, page)

    playbooks_list = list(pb.proto_partial for pb in qs)
    if not list_all:
        playbooks_list = list(pb.proto for pb in qs)

    return GetPlaybooksResponseV2(meta=get_meta(page=page, total_count=total_count), playbooks=playbooks_list)


@web_api(CreatePlaybookRequest)
@deprecated
def playbooks_create(request_message: CreatePlaybookRequest) -> Union[CreatePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    playbook: DeprecatedPlaybook = request_message.playbook
    if not playbook or not playbook.name:
        return CreatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request", description="Missing name/playbook"))
    playbook, error = deprecated_update_or_create_db_playbook(account, user.email, playbook)
    if error:
        return CreatePlaybookResponse(success=BoolValue(value=False), message=Message(title="Error", description=error))
    return CreatePlaybookResponse(success=BoolValue(value=True), playbook=playbook.deprecated_proto)


@web_api(CreatePlaybookRequestV2)
def playbooks_create_v2(request_message: CreatePlaybookRequestV2) -> Union[CreatePlaybookResponseV2, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    playbook: Playbook = request_message.playbook
    if not playbook or not playbook.name:
        return CreatePlaybookResponseV2(success=BoolValue(value=False),
                                        message=Message(title="Invalid Request", description="Missing name/playbook"))
    playbook, error = update_or_create_db_playbook(account, user.email, playbook, update_mode=False)
    if error:
        return CreatePlaybookResponseV2(success=BoolValue(value=False),
                                        message=Message(title="Error", description=error))
    return CreatePlaybookResponseV2(success=BoolValue(value=True), playbook=playbook.proto)


@web_api(UpdatePlaybookRequest)
@deprecated
def playbooks_update(request_message: UpdatePlaybookRequest) -> Union[UpdatePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    playbook_id = request_message.playbook_id.value
    update_playbook_ops = request_message.update_playbook_ops
    if not playbook_id or not update_playbook_ops:
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request", description="Missing playbook_id/ops"))
    try:
        account_playbook = account.playbook_set.get(id=playbook_id)
    except Exception as e:
        logger.error(f"Error fetching playbook: {e}")
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Error", description=str(e)))
    if account_playbook.created_by != user.email:
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request",
                                                      description="Unauthorized Action for user"))
    try:
        deprecated_playbooks_update_processor.update(account_playbook, update_playbook_ops)
    except Exception as e:
        logger.error(f"Error updating playbook: {e}")
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Error", description=str(e)))
    return UpdatePlaybookResponse(success=BoolValue(value=True))


@web_api(UpdatePlaybookRequestV2)
def playbooks_update_v2(request_message: UpdatePlaybookRequestV2) -> Union[UpdatePlaybookResponseV2, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    playbook_id = request_message.playbook_id.value
    update_playbook_ops = request_message.update_playbook_ops
    if not playbook_id or not update_playbook_ops:
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request", description="Missing playbook_id/ops"))
    try:
        account_playbook = account.playbook_set.get(id=playbook_id)
    except Exception as e:
        logger.error(f"Error fetching playbook: {e}")
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Error", description=str(e)))
    if account_playbook.created_by != user.email:
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request",
                                                      description="Unauthorized Action for user"))
    try:
        playbooks_update_processor.update(account_playbook, update_playbook_ops)
    except Exception as e:
        logger.error(f"Error updating playbook: {e}")
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Error", description=str(e)))
    return UpdatePlaybookResponse(success=BoolValue(value=True))


@web_api(ExecutePlaybookRequest)
def playbooks_execute(request_message: ExecutePlaybookRequest) -> Union[ExecutePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    current_time = current_epoch_timestamp()
    if not time_range.time_lt or not time_range.time_geq:
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    playbook_id = request_message.playbook_id.value
    if not playbook_id:
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Invalid Request", description="Missing playbook_id"))
    playbook_run_uuid = f'{str(current_time)}_{account.id}_{playbook_id}_pb_run'
    try:
        playbook_execution = create_playbook_execution(account, time_range, playbook_id, playbook_run_uuid, user.email)
    except Exception as e:
        logger.error(e)
        return ExecutePlaybookResponse(success=BoolValue(value=False),
                                       message=Message(title="Error", description=str(e)))

    saved_task = get_or_create_task(execute_playbook.__name__, account.id, playbook_id, playbook_execution.id,
                                    proto_to_dict(time_range))
    if saved_task:
        if not check_scheduled_or_running_task_run_for_task(saved_task):
            current_date_time = current_datetime()
            task = execute_playbook.delay(account.id, playbook_id, playbook_execution.id, proto_to_dict(time_range))
            try:
                saved_task_run = TaskRun.objects.create(task=saved_task, task_uuid=task.id,
                                                        status=PeriodicTaskStatus.SCHEDULED,
                                                        account_id=account.id,
                                                        scheduled_at=current_date_time)
            except Exception as e:
                logger.error(f"Exception occurred while saving task run for account: {account.id}, "
                             f"task: {saved_task.id}, error: {e}")
    else:
        logger.error(f"Failed to create task for playbook execution: {playbook_run_uuid}")
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Error",
                                                       description="Failed to create task for playbook execution"))

    return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                   playbook_run_id=StringValue(value=playbook_run_uuid))


@web_api(ExecutionPlaybookGetRequest)
@deprecated
def playbooks_execution_get(request_message: ExecutionPlaybookGetRequest) -> \
        Union[ExecutionPlaybookGetResponse, HttpResponse]:
    account: Account = get_request_account()
    playbook_run_id = request_message.playbook_run_id.value
    if not playbook_run_id:
        return ExecutionPlaybookGetResponse(success=BoolValue(value=False), message=Message(title="Invalid Request",
                                                                                            description="Missing playbook_run_id"))
    try:
        playbook_execution = get_db_playbook_execution(account, playbook_run_id=playbook_run_id)
        if not playbook_execution:
            return ExecutionPlaybookGetResponse(success=BoolValue(value=False), message=Message(title="Error",
                                                                                                description="Playbook Execution not found"))
    except Exception as e:
        return ExecutionPlaybookGetResponse(success=BoolValue(value=False),
                                            message=Message(title="Error", description=str(e)))

    playbook_execution = playbook_execution.first()
    time_range = playbook_execution.time_range
    time_range_proto = dict_to_proto(time_range, TimeRange) if time_range else TimeRange()
    return ExecutionPlaybookGetResponse(meta=get_meta(time_range_proto), success=BoolValue(value=True),
                                        playbook_execution=playbook_execution.deprecated_proto)


@web_api(ExecutionPlaybookGetRequestV2)
def playbooks_execution_get_v2(request_message: ExecutionPlaybookGetRequestV2) -> \
        Union[ExecutionPlaybookGetResponseV2, HttpResponse]:
    account: Account = get_request_account()
    playbook_run_id = request_message.playbook_run_id.value
    if not playbook_run_id:
        return ExecutionPlaybookGetResponseV2(success=BoolValue(value=False), message=Message(title="Invalid Request",
                                                                                              description="Missing playbook_run_id"))
    try:
        playbook_execution = get_db_playbook_execution(account, playbook_run_id=playbook_run_id)
        if not playbook_execution:
            return ExecutionPlaybookGetResponseV2(success=BoolValue(value=False), message=Message(title="Error",
                                                                                                  description="Playbook Execution not found"))
    except Exception as e:
        return ExecutionPlaybookGetResponseV2(success=BoolValue(value=False),
                                              message=Message(title="Error", description=str(e)))

    playbook_execution = playbook_execution.first()
    time_range = playbook_execution.time_range
    time_range_proto = dict_to_proto(time_range, TimeRange) if time_range else TimeRange()
    return ExecutionPlaybookGetResponseV2(meta=get_meta(time_range_proto), success=BoolValue(value=True),
                                          playbook_execution=playbook_execution.proto)


@web_api(ExecutionsPlaybooksListRequest)
def playbooks_executions_list(request_message: ExecutionsPlaybooksListRequest) -> \
        Union[ExecutionsPlaybooksListResponse, HttpResponse]:
    meta: Meta = request_message.meta
    page: Page = meta.page
    account: Account = get_request_account()
    playbook_ids = request_message.playbook_ids
    try:
        playbook_executions = get_db_playbook_execution(account, playbook_ids=playbook_ids)
        if not playbook_executions:
            return ExecutionsPlaybooksListResponse(success=BoolValue(value=True),
                                                   message=Message(title="No Playbook Executions Found"))
        total_count = playbook_executions.count()
        playbook_executions = playbook_executions.order_by('-created_at')
        playbook_executions = filter_page(playbook_executions, page)
        pbe_protos = [pbe.proto_partial for pbe in playbook_executions]
        return ExecutionsPlaybooksListResponse(meta=get_meta(page=page, total_count=total_count),
                                               success=BoolValue(value=True), playbook_executions=pbe_protos)
    except Exception as e:
        return ExecutionPlaybookGetResponse(success=BoolValue(value=False),
                                            message=Message(title="Error", description=str(e)))


@account_post_api(ExecutePlaybookRequest)
def playbooks_api_execute(request_message: ExecutePlaybookRequest) -> Union[ExecutePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_api_token_user()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    current_time = current_epoch_timestamp()
    if not time_range.time_lt or not time_range.time_geq:
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    playbook_id = request_message.playbook_id.value
    if not playbook_id:
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Invalid Request", description="Missing playbook_id"))
    playbook_run_uuid = f'{str(current_time)}_{account.id}_{playbook_id}_pb_run'
    try:
        playbook_execution = create_playbook_execution(account, time_range, playbook_id, playbook_run_uuid, user.email)
    except Exception as e:
        logger.error(e)
        return ExecutePlaybookResponse(success=BoolValue(value=False),
                                       message=Message(title="Error", description=str(e)))

    saved_task = get_or_create_task(execute_playbook.__name__, account.id, playbook_id, playbook_execution.id,
                                    proto_to_dict(time_range))
    if saved_task:
        if not check_scheduled_or_running_task_run_for_task(saved_task):
            current_date_time = current_datetime()
            task = execute_playbook.delay(account.id, playbook_id, playbook_execution.id, proto_to_dict(time_range))
            try:
                saved_task_run = TaskRun.objects.create(task=saved_task, task_uuid=task.id,
                                                        status=PeriodicTaskStatus.SCHEDULED,
                                                        account_id=account.id,
                                                        scheduled_at=current_date_time)
            except Exception as e:
                logger.error(f"Exception occurred while saving task run for account: {account.id}, "
                             f"task: {saved_task.id}, error: {e}")
    else:
        logger.error(f"Failed to create task for playbook execution: {playbook_run_uuid}")
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Error",
                                                       description="Failed to create task for playbook execution"))

    return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                   playbook_run_id=StringValue(value=playbook_run_uuid))


@account_get_api()
@deprecated
def playbooks_api_execution_get(request_message: HttpRequest) -> Union[ExecutionPlaybookAPIGetResponse, HttpResponse]:
    account: Account = get_request_account()
    query_dict = request_message.GET
    if 'playbook_run_id' not in query_dict:
        return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=False), message=Message(title="Invalid Request",
                                                                                               description="Missing playbook_run_id"))
    request_dict = dict(query_dict)
    playbook_run_id = request_dict.get('playbook_run_id')
    if isinstance(playbook_run_id, list):
        playbook_run_ids = playbook_run_id
    else:
        playbook_run_ids = [playbook_run_id]
    try:
        playbook_executions = get_db_playbook_execution(account, playbook_run_ids=playbook_run_ids)
        if not playbook_executions:
            return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=False), message=Message(title="Error",
                                                                                                   description="Playbook Execution not found"))
    except Exception as e:
        return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=False),
                                               message=Message(title="Error", description=str(e)))

    pe_protos = []
    for pe in playbook_executions:
        pe_protos.append(pe.deprecated_proto)
    return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=True), playbook_executions=pe_protos)


@account_get_api()
def playbooks_api_execution_get_v2(request_message: HttpRequest) -> \
        Union[ExecutionPlaybookAPIGetResponseV2, HttpResponse]:
    account: Account = get_request_account()
    query_dict = request_message.GET
    if 'playbook_run_id' not in query_dict:
        return ExecutionPlaybookAPIGetResponseV2(success=BoolValue(value=False),
                                                 message=Message(title="Invalid Request",
                                                                 description="Missing playbook_run_id"))
    request_dict = dict(query_dict)
    playbook_run_id = request_dict.get('playbook_run_id')
    if isinstance(playbook_run_id, list):
        playbook_run_ids = playbook_run_id
    else:
        playbook_run_ids = [playbook_run_id]
    try:
        playbook_executions = get_db_playbook_execution(account, playbook_run_ids=playbook_run_ids)
        if not playbook_executions:
            return ExecutionPlaybookAPIGetResponseV2(success=BoolValue(value=False), message=Message(title="Error",
                                                                                                     description="Playbook Execution not found"))
    except Exception as e:
        return ExecutionPlaybookAPIGetResponseV2(success=BoolValue(value=False),
                                                 message=Message(title="Error", description=str(e)))

    pe_protos = []
    for pe in playbook_executions:
        pe_protos.append(pe.proto)
    return ExecutionPlaybookAPIGetResponseV2(success=BoolValue(value=True), playbook_executions=pe_protos)


@csrf_exempt
@api_view(['GET'])
@get_proto_schema_validator()
def playbooks_templates(request_message: HttpRequest) -> Union[PlaybookTemplatesGetResponse, HttpResponse]:
    folder_path = settings.PLAYBOOK_TEMPLATE_PATH
    try:
        json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
        if not json_files:
            return PlaybookTemplatesGetResponse(success=BoolValue(value=False),
                                                message=Message(title="Not Found", description="No JSON files found"))

        json_contents = []
        for json_file in json_files:
            full_path = os.path.join(folder_path, json_file)
            with open(full_path, 'r') as file:
                s = Struct()
                data = json.load(file)
                s.update(data)
                json_contents.append(s)

    except Exception as e:
        return PlaybookTemplatesGetResponse(success=BoolValue(value=False),
                                            message=Message(title="Internal Error", description=str(e)))

    return PlaybookTemplatesGetResponse(success=BoolValue(value=True), data=json_contents)


@web_api(PlaybooksBuilderOptionsRequest)
def playbooks_builder_options(request_message: PlaybooksBuilderOptionsRequest) -> \
        Union[PlaybooksBuilderOptionsResponse, HttpResponse]:
    try:
        account: Account = get_request_account()
        interpreter_type_options = []

        source_options = playbook_source_facade.get_source_options(account.id)
        open_ai_connector = get_db_account_connectors(account, connector_type=ConnectorType.OPEN_AI, is_active=True)
        if open_ai_connector.exists():
            interpreter_type_options.append(
                PlaybooksBuilderOptionsResponse.InterpreterTypeOption(type=InterpreterType.LLM_CHAT_GPT_VISION_I,
                                                                      display_name=StringValue(
                                                                          value="OpenAi Vision Interpreter")))

        return PlaybooksBuilderOptionsResponse(success=BoolValue(value=True),
                                               interpreter_types=interpreter_type_options,
                                               source_options=source_options)
    except Exception as e:
        return PlaybooksBuilderOptionsResponse(success=BoolValue(value=False),
                                               message=Message(title="Error", description=str(e)))
