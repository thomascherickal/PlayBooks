# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.playbooks import playbook_pb2 as protos_dot_playbooks_dot_playbook__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aprotos/playbooks/api.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\x1a\x1fprotos/playbooks/playbook.proto\"\x80\x01\n\x16RunPlaybookTaskRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12J\n\x18playbook_task_definition\x18\x02 \x01(\x0b\x32(.protos.playbooks.PlaybookTaskDefinition\"\xd2\x01\n\x17RunPlaybookTaskResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12L\n\x15task_execution_result\x18\x04 \x01(\x0b\x32-.protos.playbooks.PlaybookTaskExecutionResultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RUNPLAYBOOKTASKREQUEST._serialized_start=133
  _RUNPLAYBOOKTASKREQUEST._serialized_end=261
  _RUNPLAYBOOKTASKRESPONSE._serialized_start=264
  _RUNPLAYBOOKTASKRESPONSE._serialized_end=474
# @@protoc_insertion_point(module_scope)
