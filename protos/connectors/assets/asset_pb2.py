# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/assets/asset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2
from protos.connectors.assets import cloudwatch_asset_pb2 as protos_dot_connectors_dot_assets_dot_cloudwatch__asset__pb2
from protos.connectors.assets import grafana_asset_pb2 as protos_dot_connectors_dot_assets_dot_grafana__asset__pb2
from protos.connectors.assets import clickhouse_asset_pb2 as protos_dot_connectors_dot_assets_dot_clickhouse__asset__pb2
from protos.connectors.assets import slack_asset_pb2 as protos_dot_connectors_dot_assets_dot_slack__asset__pb2
from protos.connectors.assets import newrelic_asset_pb2 as protos_dot_connectors_dot_assets_dot_newrelic__asset__pb2
from protos.connectors.assets import datadog_asset_pb2 as protos_dot_connectors_dot_assets_dot_datadog__asset__pb2
from protos.connectors.assets import postgres_asset_pb2 as protos_dot_connectors_dot_assets_dot_postgres__asset__pb2
from protos.connectors.assets import eks_asset_pb2 as protos_dot_connectors_dot_assets_dot_eks__asset__pb2
from protos.connectors.assets import azure_asset_pb2 as protos_dot_connectors_dot_assets_dot_azure__asset__pb2
from protos.connectors.assets import remote_server_asset_pb2 as protos_dot_connectors_dot_assets_dot_remote__server__asset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$protos/connectors/assets/asset.proto\x12\x18protos.connectors.assets\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\x1a!protos/connectors/connector.proto\x1a/protos/connectors/assets/cloudwatch_asset.proto\x1a,protos/connectors/assets/grafana_asset.proto\x1a/protos/connectors/assets/clickhouse_asset.proto\x1a*protos/connectors/assets/slack_asset.proto\x1a-protos/connectors/assets/newrelic_asset.proto\x1a,protos/connectors/assets/datadog_asset.proto\x1a-protos/connectors/assets/postgres_asset.proto\x1a(protos/connectors/assets/eks_asset.proto\x1a*protos/connectors/assets/azure_asset.proto\x1a\x32protos/connectors/assets/remote_server_asset.proto\"\xfe\n\n\x19\x43onnectorModelTypeOptions\x12+\n\nmodel_type\x18\x01 \x01(\x0e\x32\x17.protos.SourceModelType\x12\x66\n\"cloudwatch_log_group_model_options\x18\x02 \x01(\x0b\x32\x38.protos.connectors.assets.CloudwatchLogGroupAssetOptionsH\x00\x12\x61\n\x1f\x63loudwatch_metric_model_options\x18\x03 \x01(\x0b\x32\x36.protos.connectors.assets.CloudwatchMetricAssetOptionsH\x00\x12u\n*grafana_target_metric_promql_model_options\x18\x04 \x01(\x0b\x32?.protos.connectors.assets.GrafanaTargetMetricPromQlAssetOptionsH\x00\x12\x65\n!clickhouse_database_model_options\x18\x05 \x01(\x0b\x32\x38.protos.connectors.assets.ClickhouseDatabaseAssetOptionsH\x00\x12Y\n\x1bslack_channel_model_options\x18\x06 \x01(\x0b\x32\x32.protos.connectors.assets.SlackChannelAssetOptionsH\x00\x12u\n*new_relic_entity_application_model_options\x18\x07 \x01(\x0b\x32?.protos.connectors.assets.NewRelicApplicationEntityAssetOptionsH\x00\x12q\n(new_relic_entity_dashboard_model_options\x18\x08 \x01(\x0b\x32=.protos.connectors.assets.NewRelicDashboardEntityAssetOptionsH\x00\x12]\n\x1d\x64\x61tadog_service_model_options\x18\t \x01(\x0b\x32\x34.protos.connectors.assets.DatadogServiceAssetOptionsH\x00\x12\x61\n\x1fpostgres_database_model_options\x18\n \x01(\x0b\x32\x36.protos.connectors.assets.PostgresDatabaseAssetOptionsH\x00\x12U\n\x19\x65ks_cluster_model_options\x18\x0b \x01(\x0b\x32\x30.protos.connectors.assets.EksClusterAssetOptionsH\x00\x12S\n\x18ssh_server_model_options\x18\x0c \x01(\x0b\x32/.protos.connectors.assets.SshServerAssetOptionsH\x00\x12]\n\x1d\x61zure_workspace_model_options\x18\r \x01(\x0b\x32\x34.protos.connectors.assets.AzureWorkspaceAssetOptionsH\x00\x12n\n+grafana_prometheus_datasource_model_options\x18\x0e \x01(\x0b\x32\x37.protos.connectors.assets.GrafanaDatasourceAssetOptionsH\x00\x42\t\n\x07options\"\xcf\x01\n\"AccountConnectorAssetsModelOptions\x12&\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32\x0e.protos.Source\x12/\n\tconnector\x18\x02 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12P\n\x13model_types_options\x18\x03 \x03(\x0b\x32\x33.protos.connectors.assets.ConnectorModelTypeOptions\"\xda\n\n\"AccountConnectorAssetsModelFilters\x12\x66\n\"cloudwatch_log_group_model_filters\x18\x01 \x01(\x0b\x32\x38.protos.connectors.assets.CloudwatchLogGroupAssetOptionsH\x00\x12\x61\n\x1f\x63loudwatch_metric_model_filters\x18\x02 \x01(\x0b\x32\x36.protos.connectors.assets.CloudwatchMetricAssetOptionsH\x00\x12u\n*grafana_target_metric_promql_model_filters\x18\x03 \x01(\x0b\x32?.protos.connectors.assets.GrafanaTargetMetricPromQlAssetOptionsH\x00\x12\x65\n!clickhouse_database_model_filters\x18\x04 \x01(\x0b\x32\x38.protos.connectors.assets.ClickhouseDatabaseAssetOptionsH\x00\x12Y\n\x1bslack_channel_model_filters\x18\x05 \x01(\x0b\x32\x32.protos.connectors.assets.SlackChannelAssetOptionsH\x00\x12u\n*new_relic_entity_application_model_filters\x18\x06 \x01(\x0b\x32?.protos.connectors.assets.NewRelicApplicationEntityAssetOptionsH\x00\x12q\n(new_relic_entity_dashboard_model_filters\x18\x07 \x01(\x0b\x32=.protos.connectors.assets.NewRelicDashboardEntityAssetOptionsH\x00\x12]\n\x1d\x64\x61tadog_service_model_filters\x18\x08 \x01(\x0b\x32\x34.protos.connectors.assets.DatadogServiceAssetOptionsH\x00\x12\x61\n\x1fpostgres_database_model_filters\x18\t \x01(\x0b\x32\x36.protos.connectors.assets.PostgresDatabaseAssetOptionsH\x00\x12U\n\x19\x65ks_cluster_model_filters\x18\n \x01(\x0b\x32\x30.protos.connectors.assets.EksClusterAssetOptionsH\x00\x12S\n\x18ssh_server_model_filters\x18\x0b \x01(\x0b\x32/.protos.connectors.assets.SshServerAssetOptionsH\x00\x12]\n\x1d\x61zure_workspace_model_filters\x18\x0c \x01(\x0b\x32\x34.protos.connectors.assets.AzureWorkspaceAssetOptionsH\x00\x12n\n+grafana_prometheus_datasource_model_filters\x18\r \x01(\x0b\x32\x37.protos.connectors.assets.GrafanaDatasourceAssetOptionsH\x00\x42\t\n\x07\x66ilters\"\xb7\x05\n\x16\x41\x63\x63ountConnectorAssets\x12/\n\tconnector\x18\x01 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12@\n\ncloudwatch\x18\x02 \x01(\x0b\x32*.protos.connectors.assets.CloudwatchAssetsH\x00\x12:\n\x07grafana\x18\x03 \x01(\x0b\x32\'.protos.connectors.assets.GrafanaAssetsH\x00\x12@\n\nclickhouse\x18\x04 \x01(\x0b\x32*.protos.connectors.assets.ClickhouseAssetsH\x00\x12\x36\n\x05slack\x18\x05 \x01(\x0b\x32%.protos.connectors.assets.SlackAssetsH\x00\x12=\n\tnew_relic\x18\x06 \x01(\x0b\x32(.protos.connectors.assets.NewRelicAssetsH\x00\x12:\n\x07\x64\x61tadog\x18\x07 \x01(\x0b\x32\'.protos.connectors.assets.DatadogAssetsH\x00\x12<\n\x08postgres\x18\x08 \x01(\x0b\x32(.protos.connectors.assets.PostgresAssetsH\x00\x12\x32\n\x03\x65ks\x18\t \x01(\x0b\x32#.protos.connectors.assets.EksAssetsH\x00\x12\x45\n\rremote_server\x18\n \x01(\x0b\x32,.protos.connectors.assets.RemoteServerAssetsH\x00\x12\x36\n\x05\x61zure\x18\x0b \x01(\x0b\x32%.protos.connectors.assets.AzureAssetsH\x00\x42\x08\n\x06\x61ssetsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.assets.asset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONNECTORMODELTYPEOPTIONS._serialized_start=619
  _CONNECTORMODELTYPEOPTIONS._serialized_end=2025
  _ACCOUNTCONNECTORASSETSMODELOPTIONS._serialized_start=2028
  _ACCOUNTCONNECTORASSETSMODELOPTIONS._serialized_end=2235
  _ACCOUNTCONNECTORASSETSMODELFILTERS._serialized_start=2238
  _ACCOUNTCONNECTORASSETSMODELFILTERS._serialized_end=3608
  _ACCOUNTCONNECTORASSETS._serialized_start=3611
  _ACCOUNTCONNECTORASSETS._serialized_end=4306
# @@protoc_insertion_point(module_scope)
