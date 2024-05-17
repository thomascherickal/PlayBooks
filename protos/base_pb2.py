# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/base.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/base.proto\x12\x06protos\x1a\x1egoogle/protobuf/wrappers.proto\".\n\tTimeRange\x12\x10\n\x08time_geq\x18\x01 \x01(\x04\x12\x0f\n\x07time_lt\x18\x02 \x01(\x04\"a\n\x04Page\x12+\n\x05limit\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12,\n\x06offset\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\xaf\x01\n\x04Meta\x12%\n\ntime_range\x18\x01 \x01(\x0b\x32\x11.protos.TimeRange\x12\x1a\n\x04page\x18\x02 \x01(\x0b\x32\x0c.protos.Page\x12\x31\n\x0btotal_count\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x31\n\rshow_inactive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"@\n\x07Message\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\ttraceback\x18\x03 \x01(\t\"[\n\x0c\x45rrorMessage\x12)\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"\xc7\x02\n\x10TaskCronSchedule\x12-\n\x07minutes\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05hours\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x64\x61ys_of_the_week\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x64\x61ys_of_the_month\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x64\x61ys_of_the_year\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08timezone\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"I\n\x0cTaskInterval\x12\x39\n\x13interval_in_seconds\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"j\n\x0cTaskCronRule\x12*\n\x04rule\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08timezone\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue*\x9c\x05\n\x06Source\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06SENTRY\x10\x01\x12\x0b\n\x07SEGMENT\x10\x02\x12\x12\n\x0e\x45LASTIC_SEARCH\x10\x03\x12\r\n\tAMPLITUDE\x10\x04\x12\x0f\n\x0b\x41WS_KINESIS\x10\x05\x12\x0e\n\nCLOUDWATCH\x10\x06\x12\r\n\tCLEVERTAP\x10\x07\x12\x0f\n\x0bRUDDERSTACK\x10\x08\x12\x0c\n\x08MOENGAGE\x10\t\x12\t\n\x05\x43RIBL\x10\n\x12\t\n\x05KAFKA\x10\x0b\x12\x0b\n\x07\x44\x41TADOG\x10\x0c\x12\x0c\n\x08\x46ILEBEAT\x10\r\x12\x0c\n\x08LOGSTASH\x10\x0e\x12\x0b\n\x07\x46LUENTD\x10\x0f\x12\r\n\tFLUENTBIT\x10\x10\x12\x0e\n\nPAGER_DUTY\x10\x11\x12\r\n\tNEW_RELIC\x10\x12\x12\t\n\x05SLACK\x10\x13\x12\x0f\n\x0bHONEYBADGER\x10\x14\x12\x0f\n\x0bGOOGLE_CHAT\x10\x15\x12\x11\n\rDATADOG_OAUTH\x10\x16\x12\x07\n\x03GCM\x10\x17\x12\x0e\n\nPROMETHEUS\x10\x18\x12\x0f\n\x0b\x45LASTIC_APM\x10\x19\x12\x14\n\x10VICTORIA_METRICS\x10\x1a\x12\x11\n\rSLACK_CONNECT\x10\x1b\x12\x0b\n\x07GRAFANA\x10\x1c\x12\x0e\n\nCLICKHOUSE\x10\x1d\x12\x11\n\rDOCUMENTATION\x10\x1e\x12\x0c\n\x08POSTGRES\x10\x1f\x12\r\n\tOPS_GENIE\x10 \x12\x07\n\x03\x45KS\x10!\x12\x0f\n\x0b\x41GENT_PROXY\x10\"\x12\x0f\n\x0bGRAFANA_VPC\x10#\x12\x12\n\x0eGITHUB_ACTIONS\x10$\x12\x1b\n\x17SQL_DATABASE_CONNECTION\x10%\x12\x0b\n\x07OPEN_AI\x10&\x12\x11\n\rREMOTE_SERVER\x10\'\x12\x07\n\x03\x41PI\x10(\x12\x08\n\x04\x42\x41SH\x10)\x12\x11\n\rGRAFANA_MIMIR\x10+*\xe3\t\n\rSourceKeyType\x12\x0f\n\x0bUNKNOWN_SKT\x10\x00\x12\x12\n\x0eSENTRY_API_KEY\x10\x01\x12\x13\n\x0fSENTRY_ORG_SLUG\x10\x06\x12\x13\n\x0f\x44\x41TADOG_APP_KEY\x10\x02\x12\x13\n\x0f\x44\x41TADOG_API_KEY\x10\x03\x12\x16\n\x12\x44\x41TADOG_AUTH_TOKEN\x10\x0f\x12\x16\n\x12\x44\x41TADOG_API_DOMAIN\x10\x12\x12\x14\n\x10NEWRELIC_API_KEY\x10\x04\x12\x13\n\x0fNEWRELIC_APP_ID\x10\x05\x12\x16\n\x12NEWRELIC_QUERY_KEY\x10\x07\x12\x17\n\x13NEWRELIC_API_DOMAIN\x10\x13\x12\x18\n\x14SLACK_BOT_AUTH_TOKEN\x10\x08\x12\x11\n\rSLACK_CHANNEL\x10\t\x12\x18\n\x14HONEYBADGER_USERNAME\x10\n\x12\x18\n\x14HONEYBADGER_PASSWORD\x10\x0b\x12\x1a\n\x16HONEYBADGER_PROJECT_ID\x10\x0c\x12\x12\n\x0e\x41WS_ACCESS_KEY\x10\r\x12\x12\n\x0e\x41WS_SECRET_KEY\x10\x0e\x12\x0e\n\nAWS_REGION\x10\x14\x12\x18\n\x14\x41WS_ASSUMED_ROLE_ARN\x10\x17\x12\x10\n\x0c\x45KS_ROLE_ARN\x10(\x12\x1f\n\x1bGOOGLE_CHAT_BOT_OAUTH_TOKEN\x10\x10\x12\x1a\n\x16GOOGLE_CHAT_BOT_SPACES\x10\x11\x12\x10\n\x0cGRAFANA_HOST\x10\x15\x12\x13\n\x0fGRAFANA_API_KEY\x10\x16\x12\x18\n\x14\x43LICKHOUSE_INTERFACE\x10\x18\x12\x13\n\x0f\x43LICKHOUSE_HOST\x10\x19\x12\x13\n\x0f\x43LICKHOUSE_PORT\x10\x1a\x12\x13\n\x0f\x43LICKHOUSE_USER\x10\x1b\x12\x17\n\x13\x43LICKHOUSE_PASSWORD\x10\x1c\x12\x12\n\x0eGCM_PROJECT_ID\x10\x1d\x12\x13\n\x0fGCM_PRIVATE_KEY\x10\x1e\x12\x14\n\x10GCM_CLIENT_EMAIL\x10\x1f\x12\x11\n\rGCM_TOKEN_URI\x10 \x12\x11\n\rPOSTGRES_HOST\x10!\x12\x11\n\rPOSTGRES_USER\x10\"\x12\x15\n\x11POSTGRES_PASSWORD\x10#\x12\x11\n\rPOSTGRES_PORT\x10$\x12\x15\n\x11POSTGRES_DATABASE\x10%\x12\x14\n\x10POSTGRES_OPTIONS\x10&\x12&\n\"SQL_DATABASE_CONNECTION_STRING_URI\x10\'\x12\x16\n\x12PAGER_DUTY_API_KEY\x10)\x12\x15\n\x11OPS_GENIE_API_KEY\x10*\x12\x14\n\x10\x41GENT_PROXY_HOST\x10+\x12\x17\n\x13\x41GENT_PROXY_API_KEY\x10,\x12\x18\n\x14GITHUB_ACTIONS_TOKEN\x10-\x12\x10\n\x0cSLACK_APP_ID\x10.\x12\x13\n\x0fOPEN_AI_API_KEY\x10/\x12\x15\n\x11REMOTE_SERVER_PEM\x10\x31\x12\x16\n\x12REMOTE_SERVER_USER\x10\x32\x12\x16\n\x12REMOTE_SERVER_HOST\x10\x33\x12\x1a\n\x16REMOTE_SERVER_PASSWORD\x10\x34\x12\x0e\n\nMIMIR_HOST\x10\x35\x12\x12\n\x0eX_SCOPE_ORG_ID\x10\x36\x12\x0e\n\nSSL_VERIFY\x10\x37\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.base_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOURCE._serialized_start=1059
  _SOURCE._serialized_end=1727
  _SOURCEKEYTYPE._serialized_start=1730
  _SOURCEKEYTYPE._serialized_end=2981
  _TIMERANGE._serialized_start=61
  _TIMERANGE._serialized_end=107
  _PAGE._serialized_start=109
  _PAGE._serialized_end=206
  _META._serialized_start=209
  _META._serialized_end=384
  _MESSAGE._serialized_start=386
  _MESSAGE._serialized_end=450
  _ERRORMESSAGE._serialized_start=452
  _ERRORMESSAGE._serialized_end=543
  _TASKCRONSCHEDULE._serialized_start=546
  _TASKCRONSCHEDULE._serialized_end=873
  _TASKINTERVAL._serialized_start=875
  _TASKINTERVAL._serialized_end=948
  _TASKCRONRULE._serialized_start=950
  _TASKCRONRULE._serialized_end=1056
# @@protoc_insertion_point(module_scope)
