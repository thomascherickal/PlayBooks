# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/assets/grafana_asset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,protos/connectors/assets/grafana_asset.proto\x12\x18protos.connectors.assets\x1a\x1egoogle/protobuf/wrappers.proto\x1a!protos/connectors/connector.proto\"\xc6\x01\n\x0cGrafanaAsset\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x38\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32 .protos.connectors.ConnectorType\x12;\n\x04type\x18\x03 \x01(\x0e\x32-.protos.connectors.ConnectorMetadataModelType\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x14\n\x0clast_updated\x18\x05 \x01(\x04\x12\x10\n\x08metadata\x18\x06 \x01(\t\"\x95\t\n#GrafanaTargetMetricPromQlAssetModel\x12\x32\n\x0c\x64\x61shboard_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x64\x61shboard_title\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rdashboard_url\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x66\n\x10panel_promql_map\x18\x04 \x03(\x0b\x32L.protos.connectors.assets.GrafanaTargetMetricPromQlAssetModel.PanelPromqlMap\x1a\x8b\x05\n\x0cPromqlMetric\x12:\n\x14target_metric_ref_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x64\x61tasource_uid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nexpression\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12|\n\x12label_variable_map\x18\x04 \x03(\x0b\x32`.protos.connectors.assets.GrafanaTargetMetricPromQlAssetModel.PromqlMetric.QueryLabelVariableMap\x12\x85\x01\n\x17variable_values_options\x18\x05 \x03(\x0b\x32\x64.protos.connectors.assets.GrafanaTargetMetricPromQlAssetModel.PromqlMetric.QueryVariableValueOptions\x1a[\n\x19QueryVariableValueOptions\x12.\n\x08variable\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0e\n\x06values\x18\x02 \x03(\t\x1at\n\x15QueryLabelVariableMap\x12+\n\x05label\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08variable\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\xd7\x01\n\x0ePanelPromqlMap\x12.\n\x08panel_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bpanel_title\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x62\n\x0epromql_metrics\x18\x03 \x03(\x0b\x32J.protos.connectors.assets.GrafanaTargetMetricPromQlAssetModel.PromqlMetric\"\xcf\x04\n%GrafanaTargetMetricPromQlAssetOptions\x12k\n\ndashboards\x18\x01 \x03(\x0b\x32W.protos.connectors.assets.GrafanaTargetMetricPromQlAssetOptions.GrafanaDashboardOptions\x1a\xb8\x03\n\x17GrafanaDashboardOptions\x12\x32\n\x0c\x64\x61shboard_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x64\x61shboard_title\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rdashboard_url\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x82\x01\n\rpanel_options\x18\x04 \x03(\x0b\x32k.protos.connectors.assets.GrafanaTargetMetricPromQlAssetOptions.GrafanaDashboardOptions.GrafanaPanelOptions\x1ax\n\x13GrafanaPanelOptions\x12.\n\x08panel_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bpanel_title\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xba\x02\n\x11GrafanaAssetModel\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x38\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32 .protos.connectors.ConnectorType\x12;\n\x04type\x18\x03 \x01(\x0e\x32-.protos.connectors.ConnectorMetadataModelType\x12\x14\n\x0clast_updated\x18\x04 \x01(\x10\x12\x65\n\x1cgrafana_target_metric_promql\x18\x05 \x01(\x0b\x32=.protos.connectors.assets.GrafanaTargetMetricPromQlAssetModelH\x00\x42\x07\n\x05\x61sset\"L\n\rGrafanaAssets\x12;\n\x06\x61ssets\x18\x01 \x03(\x0b\x32+.protos.connectors.assets.GrafanaAssetModelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.assets.grafana_asset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GRAFANAASSET._serialized_start=142
  _GRAFANAASSET._serialized_end=340
  _GRAFANATARGETMETRICPROMQLASSETMODEL._serialized_start=343
  _GRAFANATARGETMETRICPROMQLASSETMODEL._serialized_end=1516
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PROMQLMETRIC._serialized_start=647
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PROMQLMETRIC._serialized_end=1298
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PROMQLMETRIC_QUERYVARIABLEVALUEOPTIONS._serialized_start=1089
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PROMQLMETRIC_QUERYVARIABLEVALUEOPTIONS._serialized_end=1180
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PROMQLMETRIC_QUERYLABELVARIABLEMAP._serialized_start=1182
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PROMQLMETRIC_QUERYLABELVARIABLEMAP._serialized_end=1298
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PANELPROMQLMAP._serialized_start=1301
  _GRAFANATARGETMETRICPROMQLASSETMODEL_PANELPROMQLMAP._serialized_end=1516
  _GRAFANATARGETMETRICPROMQLASSETOPTIONS._serialized_start=1519
  _GRAFANATARGETMETRICPROMQLASSETOPTIONS._serialized_end=2110
  _GRAFANATARGETMETRICPROMQLASSETOPTIONS_GRAFANADASHBOARDOPTIONS._serialized_start=1670
  _GRAFANATARGETMETRICPROMQLASSETOPTIONS_GRAFANADASHBOARDOPTIONS._serialized_end=2110
  _GRAFANATARGETMETRICPROMQLASSETOPTIONS_GRAFANADASHBOARDOPTIONS_GRAFANAPANELOPTIONS._serialized_start=1990
  _GRAFANATARGETMETRICPROMQLASSETOPTIONS_GRAFANADASHBOARDOPTIONS_GRAFANAPANELOPTIONS._serialized_end=2110
  _GRAFANAASSETMODEL._serialized_start=2113
  _GRAFANAASSETMODEL._serialized_end=2427
  _GRAFANAASSETS._serialized_start=2429
  _GRAFANAASSETS._serialized_end=2505
# @@protoc_insertion_point(module_scope)
