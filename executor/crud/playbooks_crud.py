import logging
from hashlib import md5

from django.db.utils import IntegrityError

from accounts.models import Account
from executor.models import PlayBook, PlayBookTask, PlayBookStep, PlayBookStepTaskDefinitionMapping, \
    PlayBookStepMapping
from playbooks.utils.decorators import deprecated
from protos.playbooks.intelligence_layer.interpreter_pb2 import InterpreterType
from protos.playbooks.playbook_pb2 import PlaybookTaskDefinition as PlaybookTaskDefinitionProto, \
    Playbook as PlaybookProto, PlaybookStepDefinition
from utils.proto_utils import proto_to_dict

logger = logging.getLogger(__name__)

task_type_display_map = {
    PlaybookTaskDefinitionProto.Type.UNKNOWN: "Unknown",
    PlaybookTaskDefinitionProto.Type.METRIC: "Metric",
    PlaybookTaskDefinitionProto.Type.DECISION: "Decision",
    PlaybookTaskDefinitionProto.Type.DATA_FETCH: "Data Fetch",
    PlaybookTaskDefinitionProto.Type.DOCUMENTATION: "Documentation",
    PlaybookTaskDefinitionProto.Type.ACTION: "Action",
}


@deprecated
def validate_playbook_request(playbook: PlaybookProto):
    global_variable_set = playbook.global_variable_set
    if global_variable_set:
        for global_variable_key in list(global_variable_set.keys()):
            if not global_variable_key.startswith('$'):
                return False, f"Global Variable Key {global_variable_key} should start with $"
    return True, None


@deprecated
def get_db_playbooks(account: Account, playbook_id=None, playbook_name=None, is_active=None, playbook_ids=None,
                     created_by=None):
    filters = {}
    if playbook_id:
        filters['id'] = playbook_id
    if is_active is not None:
        filters['is_active'] = is_active
    if playbook_name:
        filters['name'] = playbook_name
    if playbook_ids:
        filters['id__in'] = playbook_ids
    if created_by:
        filters['created_by'] = created_by
    try:
        return account.playbook_set.filter(**filters)
    except Exception as e:
        logger.error(f"Failed to get playbook for account_id {account.id} with error {e}")
        return None


@deprecated
def get_db_playbook_step(account: Account, playbook_id: str, playbook_step_name=None, is_active=None):
    filters = {'playbook_id': playbook_id}
    if is_active is not None:
        filters['is_active'] = is_active
    if playbook_step_name:
        filters['name'] = playbook_step_name
    try:
        return account.playbookstep_set.filter(**filters)
    except Exception as e:
        logger.error(f"Failed to get playbook steps for account_id {account.id} with error {e}")
    return None


@deprecated
def get_db_playbook_task_definitions(account: Account, playbook_id: str, playbook_step_id, is_active=None):
    filters = {'playbook_id': playbook_id, 'playbook_step_id': playbook_step_id}
    if is_active is not None:
        filters['is_active'] = is_active
    if is_active is not None:
        filters['is_active'] = is_active
    try:
        return account.playbooktask_set.filter(**filters)
    except Exception as e:
        logger.error(f"Failed to get playbook task definitions for account_id {account.id} with error {e}")
    return None


@deprecated
def update_or_create_db_playbook(account: Account, created_by, playbook: PlaybookProto, update_mode: bool = False) -> \
        (PlayBook, bool, str):
    is_valid_playbook, err = validate_playbook_request(playbook)
    if not is_valid_playbook:
        return None, f"Invalid Playbook Request: {err}"

    playbook_name = playbook.name.value
    db_playbook = get_db_playbooks(account, playbook_name=playbook_name, created_by=created_by, is_active=True)
    if db_playbook.exists() and not update_mode:
        return None, f"Playbook with name {playbook_name} already exists"

    try:
        playbook_steps: [PlaybookStepDefinition] = playbook.steps
        db_steps = []
        for step in playbook_steps:
            db_step, err = create_db_step(account, created_by, step)
            if not db_step or err:
                return None, f"Failed to create playbook step with error: {err}"
            db_steps.append(db_step)
    except Exception as e:
        return None, f"Failed to create playbook steps with error: {e}"

    global_variable_set = None
    if playbook.global_variable_set:
        global_variable_set = proto_to_dict(playbook.global_variable_set)

    description = None
    if playbook.description.value:
        description = playbook.description.value
    try:
        db_playbook, _ = PlayBook.objects.update_or_create(account=account,
                                                           name=playbook_name,
                                                           created_by=created_by,
                                                           defaults={'is_active': True,
                                                                     'global_variable_set': global_variable_set,
                                                                     'description': description
                                                                     }
                                                           )
    except Exception as e:
        return None, f"Failed to create playbook with error: {e}"

    for db_step in db_steps:
        try:
            PlayBookStepMapping.objects.create(account=account, playbook=db_playbook, playbook_step=db_step,
                                               is_active=True)
        except Exception as e:
            logger.error(f"Failed to add step {db_step.name} to playbook {db_playbook.name} with error {e}")
    return db_playbook, None


@deprecated
def create_db_step(account: Account, created_by, playbook_step: PlaybookStepDefinition) -> (PlayBookStep, str):
    try:
        tasks: [PlaybookTaskDefinitionProto] = playbook_step.tasks
        db_tasks = []
        for task in tasks:
            task_type_display = task_type_display_map.get(task.type, f"{task.type}: Unknown")
            db_task, err = get_or_create_db_task(account, created_by, task)
            if not db_task or err:
                return None, f"Failed to create task: {task_type_display} for " \
                             f"playbook step {playbook_step.name.value} with error {err}"
            db_tasks.append(db_task)

        metadata = {}
        external_links = playbook_step.external_links
        if external_links:
            el_list = []
            for el in external_links:
                el_list.append({'name': el.name.value, 'url': el.url.value})
            metadata['external_links'] = el_list

        try:
            db_step = PlayBookStep.objects.create(account=account,
                                                  name=playbook_step.name.value,
                                                  description=playbook_step.description.value,
                                                  notes=playbook_step.notes.value,
                                                  metadata=metadata,
                                                  interpreter_type=playbook_step.interpreter_type if playbook_step.interpreter_type else InterpreterType.BASIC_I,
                                                  created_by=created_by)
        except Exception as e:
            return None, f"Failed to create playbook step with error: {e}"
        for db_task in db_tasks:
            try:
                PlayBookStepTaskDefinitionMapping.objects.get_or_create(account=account,
                                                                        playbook_step=db_step,
                                                                        playbook_task_definition=db_task)
            except Exception as e:
                task_type_display = task_type_display_map.get(db_task.type, f"{db_task.type}: Unknown")
                logger.error(f"Failed to create playbook step task definition mapping for task {task_type_display} "
                             f"with error {e}")
                return None, f"Failed to create playbook step task definition mapping for task {task_type_display}"
        return db_step, None
    except Exception as e:
        return None, f"Failed to create playbook step with error: {e}"


@deprecated
def get_or_create_db_task(account: Account, created_by, task_proto: PlaybookTaskDefinitionProto) -> \
        (PlayBookTask, str):
    task_type = task_proto.type
    task_type_display = task_type_display_map.get(task_type, f"{task_type}: Unknown")
    if task_type == PlaybookTaskDefinitionProto.Type.METRIC:
        task = task_proto.metric_task
    elif task_type == PlaybookTaskDefinitionProto.Type.DECISION:
        task = task_proto.decision_task
    elif task_type == PlaybookTaskDefinitionProto.Type.DATA_FETCH:
        task = task_proto.data_fetch_task
    elif task_type == PlaybookTaskDefinitionProto.Type.DOCUMENTATION:
        task = task_proto.documentation_task
    elif task_type == PlaybookTaskDefinitionProto.Type.ACTION:
        task = task_proto.action_task
    else:
        return None, f"Invalid Task Type Received: {task_type_display}"
    task_dict = proto_to_dict(task)
    task_md5 = md5(str(task_dict).encode('utf-8')).hexdigest()
    try:
        db_task, _ = PlayBookTask.objects.get_or_create(account=account,
                                                        name=task_proto.name.value,
                                                        description=task_proto.description.value,
                                                        notes=task_proto.notes.value,
                                                        type=task_type,
                                                        task_md5=task_md5,
                                                        created_by=created_by,
                                                        defaults={'task': task_dict})
        return db_task, None
    except IntegrityError:
        db_task = PlayBookTask.objects.get(account=account, name=task_proto.name.value, task_md5=task_md5,
                                           created_by=created_by)
        return db_task, None
    except Exception as e:
        logger.error(f"Failed to create playbook task definition for task type {task_type_display} with error {e}")
    return None, f"Failed to create playbook task definition for task type: {task_type_display}"
