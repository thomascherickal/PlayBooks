import logging
import os

from accounts.models import Account
from connectors.crud.connectors_crud import get_db_account_connectors, get_db_account_connector_keys
from executor.workflows.action.notify_action_executor.notifier import Notifier
from executor.source_processors.slack_api_processor import SlackApiProcessor
from protos.base_pb2 import Source, SourceKeyType
from protos.playbooks.intelligence_layer.interpreter_pb2 import Interpretation as InterpretationProto
from protos.playbooks.workflow_pb2 import WorkflowActionNotificationConfig as WorkflowActionNotificationConfigProto, \
    WorkflowActionSlackNotificationConfig as WorkflowActionSlackNotificationConfigProto

logger = logging.getLogger(__name__)


class SlackNotifier(Notifier):

    def __init__(self, account: Account):
        self.type = WorkflowActionNotificationConfigProto.Type.SLACK
        self.account = account

        slack_connectors = get_db_account_connectors(account, connector_type=Source.SLACK, is_active=True)
        if not slack_connectors:
            raise ValueError('Slack connector is not configured for the account')
        slack_connector = slack_connectors.first()
        slack_bot_auth_token_keys = get_db_account_connector_keys(account, slack_connector.id,
                                                                  SourceKeyType.SLACK_BOT_AUTH_TOKEN)
        if not slack_bot_auth_token_keys:
            raise ValueError('Slack bot auth token is not configured for the account')

        slack_bot_auth_token = slack_bot_auth_token_keys.first().key
        self.slack_api_processor = SlackApiProcessor(slack_bot_auth_token)

    def notify(self, config: WorkflowActionNotificationConfigProto, execution_output: [InterpretationProto]):
        slack_config: WorkflowActionSlackNotificationConfigProto = config.slack_config
        channel_id = slack_config.slack_channel_id.value
        if not channel_id:
            raise ValueError('Slack channel id is not configured in the notification config')
        logger.info(f"Sending slack message to channel {channel_id} for account {self.account.id}")
        blocks = []
        file_uploads = []
        for i, interpretation in enumerate(execution_output):
            title = f'{interpretation.title.value}'
            description = interpretation.description.value
            summary = interpretation.summary.value
            block_text = title
            if description:
                block_text += f'\n{description}'
            if summary:
                block_text += f'\n{summary}'
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": block_text
                }
            })
            if interpretation.type == InterpretationProto.Type.IMAGE:
                blocks.append({
                    "type": "image",
                    "image_url": interpretation.image_url.value,
                    "alt_text": 'metric evaluation'
                })
            elif interpretation.type == InterpretationProto.Type.CSV_FILE:
                file_uploads.append({'channel_id': channel_id, 'file_path': interpretation.file_path.value,
                                     'initial_comment': interpretation.title.value})
        message_params = {'blocks': blocks, 'channel_id': channel_id}
        if slack_config.message_type == WorkflowActionSlackNotificationConfigProto.MessageType.THREAD_REPLY:
            message_params['reply_to'] = slack_config.thread_ts.value
            for file_upload in file_uploads:
                file_upload['thread_ts'] = slack_config.thread_ts.value
        try:
            self.slack_api_processor.send_bot_message(**message_params)
            for file_upload in file_uploads:
                try:
                    self.slack_api_processor.files_upload(**file_upload)
                    os.remove(file_upload['file_path'])
                except Exception as e:
                    logger.error(f"Error uploading file to slack: {e}")
                    continue
            return True
        except Exception as e:
            logger.error(f"Error sending slack message: {e}")
            raise e
