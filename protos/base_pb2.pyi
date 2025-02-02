"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Source:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SourceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Source.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _Source.ValueType  # 0
    SENTRY: _Source.ValueType  # 1
    SEGMENT: _Source.ValueType  # 2
    ELASTIC_SEARCH: _Source.ValueType  # 3
    AMPLITUDE: _Source.ValueType  # 4
    AWS_KINESIS: _Source.ValueType  # 5
    CLOUDWATCH: _Source.ValueType  # 6
    CLEVERTAP: _Source.ValueType  # 7
    RUDDERSTACK: _Source.ValueType  # 8
    MOENGAGE: _Source.ValueType  # 9
    CRIBL: _Source.ValueType  # 10
    KAFKA: _Source.ValueType  # 11
    DATADOG: _Source.ValueType  # 12
    FILEBEAT: _Source.ValueType  # 13
    LOGSTASH: _Source.ValueType  # 14
    FLUENTD: _Source.ValueType  # 15
    FLUENTBIT: _Source.ValueType  # 16
    PAGER_DUTY: _Source.ValueType  # 17
    NEW_RELIC: _Source.ValueType  # 18
    SLACK: _Source.ValueType  # 19
    HONEYBADGER: _Source.ValueType  # 20
    GOOGLE_CHAT: _Source.ValueType  # 21
    DATADOG_OAUTH: _Source.ValueType  # 22
    GCM: _Source.ValueType  # 23
    PROMETHEUS: _Source.ValueType  # 24
    ELASTIC_APM: _Source.ValueType  # 25
    VICTORIA_METRICS: _Source.ValueType  # 26
    SLACK_CONNECT: _Source.ValueType  # 27
    GRAFANA: _Source.ValueType  # 28
    CLICKHOUSE: _Source.ValueType  # 29
    DOCUMENTATION: _Source.ValueType  # 30
    POSTGRES: _Source.ValueType  # 31
    OPS_GENIE: _Source.ValueType  # 32
    EKS: _Source.ValueType  # 33
    AGENT_PROXY: _Source.ValueType  # 34
    GRAFANA_VPC: _Source.ValueType  # 35
    GITHUB_ACTIONS: _Source.ValueType  # 36
    SQL_DATABASE_CONNECTION: _Source.ValueType  # 37
    OPEN_AI: _Source.ValueType  # 38
    REMOTE_SERVER: _Source.ValueType  # 39
    API: _Source.ValueType  # 40
    BASH: _Source.ValueType  # 41
    AZURE: _Source.ValueType  # 42
    GRAFANA_MIMIR: _Source.ValueType  # 43

class Source(_Source, metaclass=_SourceEnumTypeWrapper): ...

UNKNOWN: Source.ValueType  # 0
SENTRY: Source.ValueType  # 1
SEGMENT: Source.ValueType  # 2
ELASTIC_SEARCH: Source.ValueType  # 3
AMPLITUDE: Source.ValueType  # 4
AWS_KINESIS: Source.ValueType  # 5
CLOUDWATCH: Source.ValueType  # 6
CLEVERTAP: Source.ValueType  # 7
RUDDERSTACK: Source.ValueType  # 8
MOENGAGE: Source.ValueType  # 9
CRIBL: Source.ValueType  # 10
KAFKA: Source.ValueType  # 11
DATADOG: Source.ValueType  # 12
FILEBEAT: Source.ValueType  # 13
LOGSTASH: Source.ValueType  # 14
FLUENTD: Source.ValueType  # 15
FLUENTBIT: Source.ValueType  # 16
PAGER_DUTY: Source.ValueType  # 17
NEW_RELIC: Source.ValueType  # 18
SLACK: Source.ValueType  # 19
HONEYBADGER: Source.ValueType  # 20
GOOGLE_CHAT: Source.ValueType  # 21
DATADOG_OAUTH: Source.ValueType  # 22
GCM: Source.ValueType  # 23
PROMETHEUS: Source.ValueType  # 24
ELASTIC_APM: Source.ValueType  # 25
VICTORIA_METRICS: Source.ValueType  # 26
SLACK_CONNECT: Source.ValueType  # 27
GRAFANA: Source.ValueType  # 28
CLICKHOUSE: Source.ValueType  # 29
DOCUMENTATION: Source.ValueType  # 30
POSTGRES: Source.ValueType  # 31
OPS_GENIE: Source.ValueType  # 32
EKS: Source.ValueType  # 33
AGENT_PROXY: Source.ValueType  # 34
GRAFANA_VPC: Source.ValueType  # 35
GITHUB_ACTIONS: Source.ValueType  # 36
SQL_DATABASE_CONNECTION: Source.ValueType  # 37
OPEN_AI: Source.ValueType  # 38
REMOTE_SERVER: Source.ValueType  # 39
API: Source.ValueType  # 40
BASH: Source.ValueType  # 41
AZURE: Source.ValueType  # 42
GRAFANA_MIMIR: Source.ValueType  # 43
global___Source = Source

class _SourceKeyType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SourceKeyTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SourceKeyType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_SKT: _SourceKeyType.ValueType  # 0
    SENTRY_API_KEY: _SourceKeyType.ValueType  # 1
    SENTRY_ORG_SLUG: _SourceKeyType.ValueType  # 6
    DATADOG_APP_KEY: _SourceKeyType.ValueType  # 2
    DATADOG_API_KEY: _SourceKeyType.ValueType  # 3
    DATADOG_AUTH_TOKEN: _SourceKeyType.ValueType  # 15
    DATADOG_API_DOMAIN: _SourceKeyType.ValueType  # 18
    NEWRELIC_API_KEY: _SourceKeyType.ValueType  # 4
    NEWRELIC_APP_ID: _SourceKeyType.ValueType  # 5
    NEWRELIC_QUERY_KEY: _SourceKeyType.ValueType  # 7
    NEWRELIC_API_DOMAIN: _SourceKeyType.ValueType  # 19
    SLACK_BOT_AUTH_TOKEN: _SourceKeyType.ValueType  # 8
    SLACK_CHANNEL_ID: _SourceKeyType.ValueType  # 9
    SLACK_APP_ID: _SourceKeyType.ValueType  # 46
    HONEYBADGER_USERNAME: _SourceKeyType.ValueType  # 10
    HONEYBADGER_PASSWORD: _SourceKeyType.ValueType  # 11
    HONEYBADGER_PROJECT_ID: _SourceKeyType.ValueType  # 12
    AWS_ACCESS_KEY: _SourceKeyType.ValueType  # 13
    AWS_SECRET_KEY: _SourceKeyType.ValueType  # 14
    AWS_REGION: _SourceKeyType.ValueType  # 20
    AWS_ASSUMED_ROLE_ARN: _SourceKeyType.ValueType  # 23
    EKS_ROLE_ARN: _SourceKeyType.ValueType  # 40
    GOOGLE_CHAT_BOT_OAUTH_TOKEN: _SourceKeyType.ValueType  # 16
    GOOGLE_CHAT_BOT_SPACES: _SourceKeyType.ValueType  # 17
    GRAFANA_HOST: _SourceKeyType.ValueType  # 21
    GRAFANA_API_KEY: _SourceKeyType.ValueType  # 22
    CLICKHOUSE_INTERFACE: _SourceKeyType.ValueType  # 24
    CLICKHOUSE_HOST: _SourceKeyType.ValueType  # 25
    CLICKHOUSE_PORT: _SourceKeyType.ValueType  # 26
    CLICKHOUSE_USER: _SourceKeyType.ValueType  # 27
    CLICKHOUSE_PASSWORD: _SourceKeyType.ValueType  # 28
    GCM_PROJECT_ID: _SourceKeyType.ValueType  # 29
    GCM_PRIVATE_KEY: _SourceKeyType.ValueType  # 30
    GCM_CLIENT_EMAIL: _SourceKeyType.ValueType  # 31
    GCM_TOKEN_URI: _SourceKeyType.ValueType  # 32
    POSTGRES_HOST: _SourceKeyType.ValueType  # 33
    POSTGRES_USER: _SourceKeyType.ValueType  # 34
    POSTGRES_PASSWORD: _SourceKeyType.ValueType  # 35
    POSTGRES_PORT: _SourceKeyType.ValueType  # 36
    POSTGRES_DATABASE: _SourceKeyType.ValueType  # 37
    POSTGRES_OPTIONS: _SourceKeyType.ValueType  # 38
    SQL_DATABASE_CONNECTION_STRING_URI: _SourceKeyType.ValueType  # 39
    PAGER_DUTY_API_KEY: _SourceKeyType.ValueType  # 41
    OPS_GENIE_API_KEY: _SourceKeyType.ValueType  # 42
    AGENT_PROXY_HOST: _SourceKeyType.ValueType  # 43
    AGENT_PROXY_API_KEY: _SourceKeyType.ValueType  # 44
    GITHUB_ACTIONS_TOKEN: _SourceKeyType.ValueType  # 45
    OPEN_AI_API_KEY: _SourceKeyType.ValueType  # 47
    REMOTE_SERVER_PEM: _SourceKeyType.ValueType  # 49
    REMOTE_SERVER_USER: _SourceKeyType.ValueType  # 50
    REMOTE_SERVER_HOST: _SourceKeyType.ValueType  # 51
    REMOTE_SERVER_PASSWORD: _SourceKeyType.ValueType  # 52
    MIMIR_HOST: _SourceKeyType.ValueType  # 53
    X_SCOPE_ORG_ID: _SourceKeyType.ValueType  # 54
    SSL_VERIFY: _SourceKeyType.ValueType  # 55
    AZURE_SUBSCRIPTION_ID: _SourceKeyType.ValueType  # 56
    AZURE_TENANT_ID: _SourceKeyType.ValueType  # 57
    AZURE_CLIENT_ID: _SourceKeyType.ValueType  # 58
    AZURE_CLIENT_SECRET: _SourceKeyType.ValueType  # 59

class SourceKeyType(_SourceKeyType, metaclass=_SourceKeyTypeEnumTypeWrapper): ...

UNKNOWN_SKT: SourceKeyType.ValueType  # 0
SENTRY_API_KEY: SourceKeyType.ValueType  # 1
SENTRY_ORG_SLUG: SourceKeyType.ValueType  # 6
DATADOG_APP_KEY: SourceKeyType.ValueType  # 2
DATADOG_API_KEY: SourceKeyType.ValueType  # 3
DATADOG_AUTH_TOKEN: SourceKeyType.ValueType  # 15
DATADOG_API_DOMAIN: SourceKeyType.ValueType  # 18
NEWRELIC_API_KEY: SourceKeyType.ValueType  # 4
NEWRELIC_APP_ID: SourceKeyType.ValueType  # 5
NEWRELIC_QUERY_KEY: SourceKeyType.ValueType  # 7
NEWRELIC_API_DOMAIN: SourceKeyType.ValueType  # 19
SLACK_BOT_AUTH_TOKEN: SourceKeyType.ValueType  # 8
SLACK_CHANNEL_ID: SourceKeyType.ValueType  # 9
SLACK_APP_ID: SourceKeyType.ValueType  # 46
HONEYBADGER_USERNAME: SourceKeyType.ValueType  # 10
HONEYBADGER_PASSWORD: SourceKeyType.ValueType  # 11
HONEYBADGER_PROJECT_ID: SourceKeyType.ValueType  # 12
AWS_ACCESS_KEY: SourceKeyType.ValueType  # 13
AWS_SECRET_KEY: SourceKeyType.ValueType  # 14
AWS_REGION: SourceKeyType.ValueType  # 20
AWS_ASSUMED_ROLE_ARN: SourceKeyType.ValueType  # 23
EKS_ROLE_ARN: SourceKeyType.ValueType  # 40
GOOGLE_CHAT_BOT_OAUTH_TOKEN: SourceKeyType.ValueType  # 16
GOOGLE_CHAT_BOT_SPACES: SourceKeyType.ValueType  # 17
GRAFANA_HOST: SourceKeyType.ValueType  # 21
GRAFANA_API_KEY: SourceKeyType.ValueType  # 22
CLICKHOUSE_INTERFACE: SourceKeyType.ValueType  # 24
CLICKHOUSE_HOST: SourceKeyType.ValueType  # 25
CLICKHOUSE_PORT: SourceKeyType.ValueType  # 26
CLICKHOUSE_USER: SourceKeyType.ValueType  # 27
CLICKHOUSE_PASSWORD: SourceKeyType.ValueType  # 28
GCM_PROJECT_ID: SourceKeyType.ValueType  # 29
GCM_PRIVATE_KEY: SourceKeyType.ValueType  # 30
GCM_CLIENT_EMAIL: SourceKeyType.ValueType  # 31
GCM_TOKEN_URI: SourceKeyType.ValueType  # 32
POSTGRES_HOST: SourceKeyType.ValueType  # 33
POSTGRES_USER: SourceKeyType.ValueType  # 34
POSTGRES_PASSWORD: SourceKeyType.ValueType  # 35
POSTGRES_PORT: SourceKeyType.ValueType  # 36
POSTGRES_DATABASE: SourceKeyType.ValueType  # 37
POSTGRES_OPTIONS: SourceKeyType.ValueType  # 38
SQL_DATABASE_CONNECTION_STRING_URI: SourceKeyType.ValueType  # 39
PAGER_DUTY_API_KEY: SourceKeyType.ValueType  # 41
OPS_GENIE_API_KEY: SourceKeyType.ValueType  # 42
AGENT_PROXY_HOST: SourceKeyType.ValueType  # 43
AGENT_PROXY_API_KEY: SourceKeyType.ValueType  # 44
GITHUB_ACTIONS_TOKEN: SourceKeyType.ValueType  # 45
OPEN_AI_API_KEY: SourceKeyType.ValueType  # 47
REMOTE_SERVER_PEM: SourceKeyType.ValueType  # 49
REMOTE_SERVER_USER: SourceKeyType.ValueType  # 50
REMOTE_SERVER_HOST: SourceKeyType.ValueType  # 51
REMOTE_SERVER_PASSWORD: SourceKeyType.ValueType  # 52
MIMIR_HOST: SourceKeyType.ValueType  # 53
X_SCOPE_ORG_ID: SourceKeyType.ValueType  # 54
SSL_VERIFY: SourceKeyType.ValueType  # 55
AZURE_SUBSCRIPTION_ID: SourceKeyType.ValueType  # 56
AZURE_TENANT_ID: SourceKeyType.ValueType  # 57
AZURE_CLIENT_ID: SourceKeyType.ValueType  # 58
AZURE_CLIENT_SECRET: SourceKeyType.ValueType  # 59
global___SourceKeyType = SourceKeyType

class _SourceModelType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SourceModelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SourceModelType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_MT: _SourceModelType.ValueType  # 0
    NEW_RELIC_POLICY: _SourceModelType.ValueType  # 1
    """New Relic Models"""
    NEW_RELIC_CONDITION: _SourceModelType.ValueType  # 2
    NEW_RELIC_ENTITY: _SourceModelType.ValueType  # 3
    NEW_RELIC_ENTITY_DASHBOARD: _SourceModelType.ValueType  # 4
    NEW_RELIC_ENTITY_APPLICATION: _SourceModelType.ValueType  # 5
    NEW_RELIC_NRQL: _SourceModelType.ValueType  # 6
    DATADOG_MONITOR: _SourceModelType.ValueType  # 101
    """Datadog Models"""
    DATADOG_DASHBOARD: _SourceModelType.ValueType  # 102
    DATADOG_LIVE_INTEGRATION_AWS: _SourceModelType.ValueType  # 103
    DATADOG_LIVE_INTEGRATION_AWS_LOG: _SourceModelType.ValueType  # 104
    DATADOG_LIVE_INTEGRATION_AZURE: _SourceModelType.ValueType  # 105
    DATADOG_LIVE_INTEGRATION_CLOUDFLARE: _SourceModelType.ValueType  # 106
    DATADOG_LIVE_INTEGRATION_FASTLY: _SourceModelType.ValueType  # 107
    DATADOG_LIVE_INTEGRATION_GCP: _SourceModelType.ValueType  # 108
    DATADOG_LIVE_INTEGRATION_CONFLUENT: _SourceModelType.ValueType  # 109
    DATADOG_SERVICE: _SourceModelType.ValueType  # 110
    DATADOG_METRIC: _SourceModelType.ValueType  # 111
    DATADOG_QUERY: _SourceModelType.ValueType  # 112
    CLOUDWATCH_METRIC: _SourceModelType.ValueType  # 201
    """Cloudwatch Models"""
    CLOUDWATCH_LOG_GROUP: _SourceModelType.ValueType  # 202
    GRAFANA_DATASOURCE: _SourceModelType.ValueType  # 301
    """Grafana Models"""
    GRAFANA_DASHBOARD: _SourceModelType.ValueType  # 302
    GRAFANA_TARGET_METRIC_PROMQL: _SourceModelType.ValueType  # 303
    GRAFANA_PROMETHEUS_DATASOURCE: _SourceModelType.ValueType  # 304
    CLICKHOUSE_DATABASE: _SourceModelType.ValueType  # 401
    """Clickhouse Models"""
    SLACK_CHANNEL: _SourceModelType.ValueType  # 501
    """Slack Models"""
    MARKDOWN: _SourceModelType.ValueType  # 601
    """Documentation Models"""
    IFRAME: _SourceModelType.ValueType  # 602
    POSTGRES_QUERY: _SourceModelType.ValueType  # 701
    """Postgres Models"""
    EKS_CLUSTER: _SourceModelType.ValueType  # 801
    """EKS Models"""
    SQL_DATABASE_CONNECTION_RAW_QUERY: _SourceModelType.ValueType  # 901
    """Sql Database Connection Models"""
    AZURE_WORKSPACE: _SourceModelType.ValueType  # 1001
    """Azure Models"""
    SSH_SERVER: _SourceModelType.ValueType  # 1100
    """Remote Server Models"""
    GRAFANA_MIMIR_PROMQL: _SourceModelType.ValueType  # 1201
    """Mimir Server Models"""

class SourceModelType(_SourceModelType, metaclass=_SourceModelTypeEnumTypeWrapper): ...

UNKNOWN_MT: SourceModelType.ValueType  # 0
NEW_RELIC_POLICY: SourceModelType.ValueType  # 1
"""New Relic Models"""
NEW_RELIC_CONDITION: SourceModelType.ValueType  # 2
NEW_RELIC_ENTITY: SourceModelType.ValueType  # 3
NEW_RELIC_ENTITY_DASHBOARD: SourceModelType.ValueType  # 4
NEW_RELIC_ENTITY_APPLICATION: SourceModelType.ValueType  # 5
NEW_RELIC_NRQL: SourceModelType.ValueType  # 6
DATADOG_MONITOR: SourceModelType.ValueType  # 101
"""Datadog Models"""
DATADOG_DASHBOARD: SourceModelType.ValueType  # 102
DATADOG_LIVE_INTEGRATION_AWS: SourceModelType.ValueType  # 103
DATADOG_LIVE_INTEGRATION_AWS_LOG: SourceModelType.ValueType  # 104
DATADOG_LIVE_INTEGRATION_AZURE: SourceModelType.ValueType  # 105
DATADOG_LIVE_INTEGRATION_CLOUDFLARE: SourceModelType.ValueType  # 106
DATADOG_LIVE_INTEGRATION_FASTLY: SourceModelType.ValueType  # 107
DATADOG_LIVE_INTEGRATION_GCP: SourceModelType.ValueType  # 108
DATADOG_LIVE_INTEGRATION_CONFLUENT: SourceModelType.ValueType  # 109
DATADOG_SERVICE: SourceModelType.ValueType  # 110
DATADOG_METRIC: SourceModelType.ValueType  # 111
DATADOG_QUERY: SourceModelType.ValueType  # 112
CLOUDWATCH_METRIC: SourceModelType.ValueType  # 201
"""Cloudwatch Models"""
CLOUDWATCH_LOG_GROUP: SourceModelType.ValueType  # 202
GRAFANA_DATASOURCE: SourceModelType.ValueType  # 301
"""Grafana Models"""
GRAFANA_DASHBOARD: SourceModelType.ValueType  # 302
GRAFANA_TARGET_METRIC_PROMQL: SourceModelType.ValueType  # 303
GRAFANA_PROMETHEUS_DATASOURCE: SourceModelType.ValueType  # 304
CLICKHOUSE_DATABASE: SourceModelType.ValueType  # 401
"""Clickhouse Models"""
SLACK_CHANNEL: SourceModelType.ValueType  # 501
"""Slack Models"""
MARKDOWN: SourceModelType.ValueType  # 601
"""Documentation Models"""
IFRAME: SourceModelType.ValueType  # 602
POSTGRES_QUERY: SourceModelType.ValueType  # 701
"""Postgres Models"""
EKS_CLUSTER: SourceModelType.ValueType  # 801
"""EKS Models"""
SQL_DATABASE_CONNECTION_RAW_QUERY: SourceModelType.ValueType  # 901
"""Sql Database Connection Models"""
AZURE_WORKSPACE: SourceModelType.ValueType  # 1001
"""Azure Models"""
SSH_SERVER: SourceModelType.ValueType  # 1100
"""Remote Server Models"""
GRAFANA_MIMIR_PROMQL: SourceModelType.ValueType  # 1201
"""Mimir Server Models"""
global___SourceModelType = SourceModelType

@typing_extensions.final
class TimeRange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_GEQ_FIELD_NUMBER: builtins.int
    TIME_LT_FIELD_NUMBER: builtins.int
    time_geq: builtins.int
    time_lt: builtins.int
    def __init__(
        self,
        *,
        time_geq: builtins.int = ...,
        time_lt: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["time_geq", b"time_geq", "time_lt", b"time_lt"]) -> None: ...

global___TimeRange = TimeRange

@typing_extensions.final
class Page(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    @property
    def limit(self) -> google.protobuf.wrappers_pb2.UInt32Value: ...
    @property
    def offset(self) -> google.protobuf.wrappers_pb2.UInt32Value: ...
    def __init__(
        self,
        *,
        limit: google.protobuf.wrappers_pb2.UInt32Value | None = ...,
        offset: google.protobuf.wrappers_pb2.UInt32Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["limit", b"limit", "offset", b"offset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["limit", b"limit", "offset", b"offset"]) -> None: ...

global___Page = Page

@typing_extensions.final
class Meta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_RANGE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    SHOW_INACTIVE_FIELD_NUMBER: builtins.int
    @property
    def time_range(self) -> global___TimeRange: ...
    @property
    def page(self) -> global___Page: ...
    @property
    def total_count(self) -> google.protobuf.wrappers_pb2.UInt32Value: ...
    @property
    def show_inactive(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    def __init__(
        self,
        *,
        time_range: global___TimeRange | None = ...,
        page: global___Page | None = ...,
        total_count: google.protobuf.wrappers_pb2.UInt32Value | None = ...,
        show_inactive: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page", "show_inactive", b"show_inactive", "time_range", b"time_range", "total_count", b"total_count"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["page", b"page", "show_inactive", b"show_inactive", "time_range", b"time_range", "total_count", b"total_count"]) -> None: ...

global___Meta = Meta

@typing_extensions.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TRACEBACK_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    traceback: builtins.str
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        traceback: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "title", b"title", "traceback", b"traceback"]) -> None: ...

global___Message = Message

@typing_extensions.final
class ErrorMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> global___Message: ...
    def __init__(
        self,
        *,
        error: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: global___Message | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error", b"error", "message", b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "message", b"message"]) -> None: ...

global___ErrorMessage = ErrorMessage

@typing_extensions.final
class TaskCronSchedule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MINUTES_FIELD_NUMBER: builtins.int
    HOURS_FIELD_NUMBER: builtins.int
    DAYS_OF_THE_WEEK_FIELD_NUMBER: builtins.int
    DAYS_OF_THE_MONTH_FIELD_NUMBER: builtins.int
    DAYS_OF_THE_YEAR_FIELD_NUMBER: builtins.int
    TIMEZONE_FIELD_NUMBER: builtins.int
    @property
    def minutes(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def hours(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def days_of_the_week(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def days_of_the_month(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def days_of_the_year(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def timezone(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        minutes: google.protobuf.wrappers_pb2.StringValue | None = ...,
        hours: google.protobuf.wrappers_pb2.StringValue | None = ...,
        days_of_the_week: google.protobuf.wrappers_pb2.StringValue | None = ...,
        days_of_the_month: google.protobuf.wrappers_pb2.StringValue | None = ...,
        days_of_the_year: google.protobuf.wrappers_pb2.StringValue | None = ...,
        timezone: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["days_of_the_month", b"days_of_the_month", "days_of_the_week", b"days_of_the_week", "days_of_the_year", b"days_of_the_year", "hours", b"hours", "minutes", b"minutes", "timezone", b"timezone"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["days_of_the_month", b"days_of_the_month", "days_of_the_week", b"days_of_the_week", "days_of_the_year", b"days_of_the_year", "hours", b"hours", "minutes", b"minutes", "timezone", b"timezone"]) -> None: ...

global___TaskCronSchedule = TaskCronSchedule

@typing_extensions.final
class TaskInterval(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERVAL_IN_SECONDS_FIELD_NUMBER: builtins.int
    @property
    def interval_in_seconds(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    def __init__(
        self,
        *,
        interval_in_seconds: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["interval_in_seconds", b"interval_in_seconds"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["interval_in_seconds", b"interval_in_seconds"]) -> None: ...

global___TaskInterval = TaskInterval

@typing_extensions.final
class TaskCronRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RULE_FIELD_NUMBER: builtins.int
    TIMEZONE_FIELD_NUMBER: builtins.int
    @property
    def rule(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def timezone(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        rule: google.protobuf.wrappers_pb2.StringValue | None = ...,
        timezone: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rule", b"rule", "timezone", b"timezone"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["rule", b"rule", "timezone", b"timezone"]) -> None: ...

global___TaskCronRule = TaskCronRule
