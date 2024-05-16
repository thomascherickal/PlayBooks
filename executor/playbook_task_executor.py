from typing import Dict

from protos.base_pb2 import TimeRange, Source
from protos.playbooks.playbook_commons_pb2 import PlaybookTaskResult
from protos.playbooks.playbook_v2_pb2 import PlaybookTask


class PlaybookTaskExecutor:
    source: Source = Source.UNKNOWN
    task_type_callable_map = {}

    @classmethod
    def get_task_type_callable_map(cls):
        return cls.task_type_callable_map

    def execute(self, time_range: TimeRange, global_variable_set: Dict, task: PlaybookTask) -> PlaybookTaskResult:
        pass
