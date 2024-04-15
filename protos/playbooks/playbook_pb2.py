# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/playbook.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fprotos/playbooks/playbook.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf3\x0c\n!PlaybookMetricTaskExecutionResult\x12L\n\rmetric_source\x18\x01 \x01(\x0e\x32\x35.protos.playbooks.PlaybookMetricTaskDefinition.Source\x12\x31\n\x0bmetric_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11metric_expression\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12J\n\x06result\x18\x05 \x01(\x0b\x32:.protos.playbooks.PlaybookMetricTaskExecutionResult.Result\x1a\xc7\n\n\x06Result\x12M\n\x04type\x18\x01 \x01(\x0e\x32?.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.Type\x12[\n\ntimeseries\x18\x02 \x01(\x0b\x32\x45.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.TimeseriesH\x00\x12^\n\x0ctable_result\x18\x03 \x01(\x0b\x32\x46.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.TableResultH\x00\x1al\n\x11GroupByLabelValue\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x8c\x04\n\nTimeseries\x12\x80\x01\n\x19labeled_metric_timeseries\x18\x03 \x03(\x0b\x32].protos.playbooks.PlaybookMetricTaskExecutionResult.Result.Timeseries.LabeledMetricTimeseries\x1a\xfa\x02\n\x17LabeledMetricTimeseries\x12i\n\x13metric_label_values\x18\x01 \x03(\x0b\x32L.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.GroupByLabelValue\x12*\n\x04unit\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12{\n\ndatapoints\x18\x03 \x03(\x0b\x32g.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.Timeseries.LabeledMetricTimeseries.Datapoint\x1aK\n\tDatapoint\x12\x11\n\ttimestamp\x18\x01 \x01(\x10\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xf2\x02\n\x0bTableResult\x12]\n\x04rows\x18\x01 \x03(\x0b\x32O.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.TableResult.TableRow\x1a\x92\x01\n\x0bTableColumn\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04type\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1ao\n\x08TableRow\x12\x63\n\x07\x63olumns\x18\x01 \x03(\x0b\x32R.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.TableResult.TableColumn\"5\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nTIMESERIES\x10\x01\x12\x10\n\x0cTABLE_RESULT\x10\x02\x42\x08\n\x06result\"\xbc\x07\n#PlaybookDecisionTaskExecutionResult\x12\x36\n\x10\x64\x65\x63ision_task_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x38\n\x12\x64\x65\x63ision_task_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12L\n\x06result\x18\x03 \x01(\x0b\x32<.protos.playbooks.PlaybookDecisionTaskExecutionResult.Result\x1a\xd4\x05\n\x06Result\x12O\n\x04type\x18\x01 \x01(\x0e\x32\x41.protos.playbooks.PlaybookDecisionTaskExecutionResult.Result.Type\x12/\n\tnext_task\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12p\n\x19\x65lse_evaluation_condition\x18\x03 \x01(\x0b\x32K.protos.playbooks.PlaybookDecisionTaskExecutionResult.Result.ElseEvaluationH\x00\x12|\n\x1ftimeseries_evaluation_condition\x18\x04 \x01(\x0b\x32Q.protos.playbooks.PlaybookDecisionTaskExecutionResult.Result.TimeseriesEvaluationH\x00\x1a@\n\x0e\x45lseEvaluation\x12.\n\nevaluation\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a\xb2\x01\n\x14TimeseriesEvaluation\x12.\n\nevaluation\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x04rule\x18\x02 \x01(\x0b\x32/.protos.playbooks.TimeseriesEvaluationTask.Rule\x12+\n\x05value\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"W\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1d\n\x19\x45LSE_EVALUATION_CONDITION\x10\x01\x12#\n\x1fTIMESERIES_EVALUATION_CONDITION\x10\x02\x42\x08\n\x06result\"\xe5\x08\n$PlaybookDataFetchTaskExecutionResult\x12\x38\n\x12\x64\x61ta_fetch_task_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12:\n\x14\x64\x61ta_fetch_task_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12M\n\x0b\x64\x61ta_source\x18\x03 \x01(\x0e\x32\x38.protos.playbooks.PlaybookDataFetchTaskDefinition.Source\x12M\n\x06result\x18\x04 \x01(\x0b\x32=.protos.playbooks.PlaybookDataFetchTaskExecutionResult.Result\x1a\xa8\x06\n\x06Result\x12P\n\x04type\x18\x01 \x01(\x0e\x32\x42.protos.playbooks.PlaybookDataFetchTaskExecutionResult.Result.Type\x12\x61\n\x0ctable_result\x18\x02 \x01(\x0b\x32I.protos.playbooks.PlaybookDataFetchTaskExecutionResult.Result.TableResultH\x00\x1a\xb7\x04\n\x0bTableResult\x12/\n\traw_query\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0btotal_count\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12+\n\x05limit\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12,\n\x06offset\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12`\n\x04rows\x18\x05 \x03(\x0b\x32R.protos.playbooks.PlaybookDataFetchTaskExecutionResult.Result.TableResult.TableRow\x1a\x92\x01\n\x0bTableColumn\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04type\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1ar\n\x08TableRow\x12\x66\n\x07\x63olumns\x18\x01 \x03(\x0b\x32U.protos.playbooks.PlaybookDataFetchTaskExecutionResult.Result.TableResult.TableColumn\"%\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cTABLE_RESULT\x10\x01\x42\x08\n\x06result\"\xad\x04\n(PlaybookDocumentationTaskExecutionResult\x12;\n\x15\x64ocumentation_task_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12=\n\x17\x64ocumentation_task_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12Q\n\x06result\x18\x03 \x01(\x0b\x32\x41.protos.playbooks.PlaybookDocumentationTaskExecutionResult.Result\x1a\xb1\x02\n\x06Result\x12T\n\x04type\x18\x01 \x01(\x0e\x32\x46.protos.playbooks.PlaybookDocumentationTaskExecutionResult.Result.Type\x12k\n\x0fmarkdown_result\x18\x02 \x01(\x0b\x32P.protos.playbooks.PlaybookDocumentationTaskExecutionResult.Result.MarkdownResultH\x00\x1a\x37\n\x0eMarkdownResult\x12%\n\x04text\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"!\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x42\x08\n\x06result\"\xe1\x03\n\x1bPlaybookTaskExecutionResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12[\n\x1cmetric_task_execution_result\x18\x02 \x01(\x0b\x32\x33.protos.playbooks.PlaybookMetricTaskExecutionResultH\x00\x12_\n\x1e\x64\x65\x63ision_task_execution_result\x18\x03 \x01(\x0b\x32\x35.protos.playbooks.PlaybookDecisionTaskExecutionResultH\x00\x12\x62\n data_fetch_task_execution_result\x18\x04 \x01(\x0b\x32\x36.protos.playbooks.PlaybookDataFetchTaskExecutionResultH\x00\x12i\n#documentation_task_execution_result\x18\x05 \x01(\x0b\x32:.protos.playbooks.PlaybookDocumentationTaskExecutionResultH\x00\x42\x08\n\x06result\"\x9d\x08\n\x16PlaybookCloudwatchTask\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.protos.playbooks.PlaybookCloudwatchTask.TaskType\x12g\n\x15metric_execution_task\x18\x02 \x01(\x0b\x32\x46.protos.playbooks.PlaybookCloudwatchTask.CloudwatchMetricExecutionTaskH\x00\x12h\n\x16\x66ilter_log_events_task\x18\x03 \x01(\x0b\x32\x46.protos.playbooks.PlaybookCloudwatchTask.CloudwatchFilterLogEventsTaskH\x00\x1a\xe6\x03\n\x1d\x43loudwatchMetricExecutionTask\x12/\n\tnamespace\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06region\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bmetric_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x64\n\ndimensions\x18\x04 \x03(\x0b\x32P.protos.playbooks.PlaybookCloudwatchTask.CloudwatchMetricExecutionTask.Dimension\x12/\n\tstatistic\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x64\n\tDimension\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\xb7\x01\n\x1d\x43loudwatchFilterLogEventsTask\x12,\n\x06region\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0elog_group_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x66ilter_query\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"D\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10METRIC_EXECUTION\x10\x01\x12\x15\n\x11\x46ILTER_LOG_EVENTS\x10\x02\x42\x06\n\x04task\"\xa4\x07\n\x13PlaybookGrafanaTask\x12<\n\x04type\x18\x01 \x01(\x0e\x32..protos.playbooks.PlaybookGrafanaTask.TaskType\x12\x34\n\x0e\x64\x61tasource_uid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12g\n\x1cpromql_metric_execution_task\x18\x03 \x01(\x0b\x32?.protos.playbooks.PlaybookGrafanaTask.PromQlMetricExecutionTaskH\x00\x1a\xf1\x04\n\x19PromQlMetricExecutionTask\x12\x37\n\x11promql_expression\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12n\n\x1apromql_label_option_values\x18\x02 \x03(\x0b\x32J.protos.playbooks.PlaybookGrafanaTask.PromQlMetricExecutionTask.LabelValue\x12\x33\n\rdashboard_uid\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x64\x61shboard_title\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08panel_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bpanel_title\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x17panel_promql_expression\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x65\n\nLabelValue\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"4\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1b\n\x17PROMQL_METRIC_EXECUTION\x10\x01\x42\x06\n\x04task\"\xbf\x0e\n\x14PlaybookNewRelicTask\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.protos.playbooks.PlaybookNewRelicTask.TaskType\x12\x8c\x01\n/entity_application_golden_metric_execution_task\x18\x02 \x01(\x0b\x32Q.protos.playbooks.PlaybookNewRelicTask.EntityApplicationGoldenMetricExecutionTaskH\x00\x12\x91\x01\n2entity_dashboard_widget_nrql_metric_execution_task\x18\x03 \x01(\x0b\x32S.protos.playbooks.PlaybookNewRelicTask.EntityDashboardWidgetNRQLMetricExecutionTaskH\x00\x12\x64\n\x1anrql_metric_execution_task\x18\x04 \x01(\x0b\x32>.protos.playbooks.PlaybookNewRelicTask.NRQLMetricExecutionTaskH\x00\x1a\x9b\x03\n*EntityApplicationGoldenMetricExecutionTask\x12=\n\x17\x61pplication_entity_guid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x17\x61pplication_entity_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12golden_metric_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12golden_metric_unit\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x43\n\x1dgolden_metric_nrql_expression\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\xb6\x04\n,EntityDashboardWidgetNRQLMetricExecutionTask\x12\x34\n\x0e\x64\x61shboard_guid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x64\x61shboard_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tpage_guid\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tpage_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\twidget_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cwidget_title\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bwidget_type\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\x16widget_nrql_expression\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04unit\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\xe7\x01\n\x17NRQLMetricExecutionTask\x12\x31\n\x0bmetric_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fnrql_expression\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04unit\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x95\x01\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12.\n*ENTITY_APPLICATION_GOLDEN_METRIC_EXECUTION\x10\x01\x12\x31\n-ENTITY_DASHBOARD_WIDGET_NRQL_METRIC_EXECUTION\x10\x02\x12\x19\n\x15NRQL_METRIC_EXECUTION\x10\x03\x42\x06\n\x04task\"\xa3\x04\n\x13PlaybookDatadogTask\x12<\n\x04type\x18\x01 \x01(\x0e\x32..protos.playbooks.PlaybookDatadogTask.TaskType\x12i\n\x1dservice_metric_execution_task\x18\x02 \x01(\x0b\x32@.protos.playbooks.PlaybookDatadogTask.ServiceMetricExecutionTaskH\x00\x1a\xa3\x02\n\x1aServiceMetricExecutionTask\x12\x32\n\x0cservice_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x65nvironment_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rmetric_family\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06metric\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"5\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1c\n\x18SERVICE_METRIC_EXECUTION\x10\x01\x42\x06\n\x04task\"\xd3\x03\n\x1cPlaybookMetricTaskDefinition\x12\x45\n\x06source\x18\x01 \x01(\x0e\x32\x35.protos.playbooks.PlaybookMetricTaskDefinition.Source\x12\x43\n\x0f\x63loudwatch_task\x18\x06 \x01(\x0b\x32(.protos.playbooks.PlaybookCloudwatchTaskH\x00\x12=\n\x0cgrafana_task\x18\x07 \x01(\x0b\x32%.protos.playbooks.PlaybookGrafanaTaskH\x00\x12@\n\x0enew_relic_task\x18\x08 \x01(\x0b\x32&.protos.playbooks.PlaybookNewRelicTaskH\x00\x12=\n\x0c\x64\x61tadog_task\x18\t \x01(\x0b\x32%.protos.playbooks.PlaybookDatadogTaskH\x00\"_\n\x06Source\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nCLOUDWATCH\x10\x01\x12\x0b\n\x07GRAFANA\x10\x02\x12\r\n\tNEW_RELIC\x10\x03\x12\x0b\n\x07\x44\x41TADOG\x10\x04\x12\x0f\n\x0bGRAFANA_VPC\x10\x05\x42\x06\n\x04task\"\xaf\x06\n\x18TimeseriesEvaluationTask\x12>\n\x05rules\x18\x01 \x03(\x0b\x32/.protos.playbooks.TimeseriesEvaluationTask.Rule\x12H\n\ninput_type\x18\x02 \x01(\x0e\x32\x34.protos.playbooks.TimeseriesEvaluationTask.InputType\x12V\n\x17metric_timeseries_input\x18\x03 \x01(\x0b\x32\x33.protos.playbooks.PlaybookMetricTaskExecutionResultH\x00\x1a\xf6\x03\n\x04Rule\x12\x42\n\x04type\x18\x01 \x01(\x0e\x32\x34.protos.playbooks.TimeseriesEvaluationTask.Rule.Type\x12?\n\x08\x66unction\x18\x02 \x01(\x0e\x32-.protos.playbooks.EvaluationConditionFunction\x12?\n\x08operator\x18\x03 \x01(\x0e\x32-.protos.playbooks.EvaluationConditionOperator\x12,\n\x06window\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\tthreshold\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\tnext_task\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x62\n\x0clabel_values\x18\x07 \x03(\x0b\x32L.protos.playbooks.PlaybookMetricTaskExecutionResult.Result.GroupByLabelValue\"4\n\x04Type\x12\x0f\n\x0bUNKNOWN_TEC\x10\x00\x12\x0b\n\x07ROLLING\x10\x01\x12\x0e\n\nCUMULATIVE\x10\x02\"/\n\tInputType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x15\n\x11METRIC_TIMESERIES\x10\x01\x42\x07\n\x05input\"E\n\x12\x45lseEvaluationTask\x12/\n\tnext_task\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xc7\x01\n#PlaybookDocumentationTaskDefinition\x12H\n\x04type\x18\x01 \x01(\x0e\x32:.protos.playbooks.PlaybookDocumentationTaskDefinition.Type\x12\x33\n\rdocumentation\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"!\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\"\xdb\x02\n\x1ePlaybookDecisionTaskDefinition\x12X\n\x0f\x65valuation_type\x18\x01 \x01(\x0e\x32?.protos.playbooks.PlaybookDecisionTaskDefinition.EvaluationType\x12\x44\n\x14\x65lse_evaluation_task\x18\x02 \x01(\x0b\x32$.protos.playbooks.ElseEvaluationTaskH\x00\x12P\n\x1atimeseries_evaluation_task\x18\x03 \x01(\x0b\x32*.protos.playbooks.TimeseriesEvaluationTaskH\x00\":\n\x0e\x45valuationType\x12\x0e\n\nUNKNOWN_ET\x10\x00\x12\x08\n\x04\x45LSE\x10\x01\x12\x0e\n\nTIMESERIES\x10\x02\x42\x0b\n\tcondition\"~\n\x1fPlaybookClickhouseDataFetchTask\x12.\n\x08\x64\x61tabase\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05query\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"|\n\x1dPlaybookPostgresDataFetchTask\x12.\n\x08\x64\x61tabase\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05query\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8a\x03\n\x18PlaybookEksDataFetchTask\x12L\n\x0c\x63ommand_type\x18\x01 \x01(\x0e\x32\x36.protos.playbooks.PlaybookEksDataFetchTask.CommandType\x12\x31\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06region\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x63luster\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tnamespace\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"_\n\x0b\x43ommandType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08GET_PODS\x10\x01\x12\x13\n\x0fGET_DEPLOYMENTS\x10\x02\x12\x0e\n\nGET_EVENTS\x10\x03\x12\x10\n\x0cGET_SERVICES\x10\x04\"\xbc\x04\n\x1fPlaybookDataFetchTaskDefinition\x12H\n\x06source\x18\x01 \x01(\x0e\x32\x38.protos.playbooks.PlaybookDataFetchTaskDefinition.Source\x12\x35\n\x0forder_by_column\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05limit\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12,\n\x06offset\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12W\n\x1a\x63lickhouse_data_fetch_task\x18\x05 \x01(\x0b\x32\x31.protos.playbooks.PlaybookClickhouseDataFetchTaskH\x00\x12S\n\x18postgres_data_fetch_task\x18\x06 \x01(\x0b\x32/.protos.playbooks.PlaybookPostgresDataFetchTaskH\x00\x12I\n\x13\x65ks_data_fetch_task\x18\x07 \x01(\x0b\x32*.protos.playbooks.PlaybookEksDataFetchTaskH\x00\"<\n\x06Source\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nCLICKHOUSE\x10\x01\x12\x0c\n\x08POSTGRES\x10\x02\x12\x07\n\x03\x45KS\x10\x03\x42\x06\n\x04task\"\xd0\x05\n\x16PlaybookTaskDefinition\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05notes\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x13global_variable_set\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12;\n\x04type\x18\x06 \x01(\x0e\x32-.protos.playbooks.PlaybookTaskDefinition.Type\x12\x45\n\x0bmetric_task\x18\x07 \x01(\x0b\x32..protos.playbooks.PlaybookMetricTaskDefinitionH\x00\x12I\n\rdecision_task\x18\x08 \x01(\x0b\x32\x30.protos.playbooks.PlaybookDecisionTaskDefinitionH\x00\x12L\n\x0f\x64\x61ta_fetch_task\x18\t \x01(\x0b\x32\x31.protos.playbooks.PlaybookDataFetchTaskDefinitionH\x00\x12S\n\x12\x64ocumentation_task\x18\n \x01(\x0b\x32\x35.protos.playbooks.PlaybookDocumentationTaskDefinitionH\x00\"P\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06METRIC\x10\x01\x12\x0c\n\x08\x44\x45\x43ISION\x10\x02\x12\x0e\n\nDATA_FETCH\x10\x03\x12\x11\n\rDOCUMENTATION\x10\x04\x42\x06\n\x04task\"\x90\x03\n\x16PlaybookStepDefinition\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12M\n\x0e\x65xternal_links\x18\x04 \x03(\x0b\x32\x35.protos.playbooks.PlaybookStepDefinition.ExternalLink\x12\x37\n\x05tasks\x18\x05 \x03(\x0b\x32(.protos.playbooks.PlaybookTaskDefinition\x1a\x65\n\x0c\x45xternalLink\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03url\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xc4\x03\n\x08Playbook\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tis_active\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\ncreated_by\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\ncreated_at\x18\x05 \x01(\x10\x12\x13\n\x0blast_run_at\x18\x06 \x01(\x10\x12\x37\n\x06status\x18\x07 \x01(\x0e\x32\'.protos.playbooks.PlaybookRunStatusType\x12\x37\n\x05steps\x18\x08 \x03(\x0b\x32(.protos.playbooks.PlaybookStepDefinition\x12\x34\n\x13global_variable_set\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x30\n\x0chas_triggers\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"U\n\x0ePlaybookRunLog\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x17\n\x0fplaybook_run_id\x18\x04 \x01(\t\"\xa3\x01\n\x0bPlaybookRun\x12.\n\x04logs\x18\x01 \x03(\x0b\x32 .protos.playbooks.PlaybookRunLog\x12\x37\n\x06status\x18\x02 \x01(\x0e\x32\'.protos.playbooks.PlaybookRunStatusType\x12\x12\n\nstarted_at\x18\x03 \x01(\x04\x12\x17\n\x0fplaybook_run_id\x18\x04 \x01(\t\"\xb4\x07\n\x10UpdatePlaybookOp\x12\x31\n\x02op\x18\x01 \x01(\x0e\x32%.protos.playbooks.UpdatePlaybookOp.Op\x12U\n\x14update_playbook_name\x18\x02 \x01(\x0b\x32\x35.protos.playbooks.UpdatePlaybookOp.UpdatePlaybookNameH\x00\x12Y\n\x16update_playbook_status\x18\x03 \x01(\x0b\x32\x37.protos.playbooks.UpdatePlaybookOp.UpdatePlaybookStatusH\x00\x12L\n\x0fupdate_playbook\x18\x04 \x01(\x0b\x32\x31.protos.playbooks.UpdatePlaybookOp.UpdatePlaybookH\x00\x12z\n(update_playbook_alert_ops_trigger_status\x18\x05 \x01(\x0b\x32\x46.protos.playbooks.UpdatePlaybookOp.UpdatePlaybookAlertOpsTriggerStatusH\x00\x1a@\n\x12UpdatePlaybookName\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x45\n\x14UpdatePlaybookStatus\x12-\n\tis_active\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a>\n\x0eUpdatePlaybook\x12,\n\x08playbook\x18\x01 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\x1a\x90\x01\n#UpdatePlaybookAlertOpsTriggerStatus\x12:\n\x14\x61lert_ops_trigger_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12-\n\tis_active\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x8a\x01\n\x02Op\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x18\n\x14UPDATE_PLAYBOOK_NAME\x10\x01\x12\x1a\n\x16UPDATE_PLAYBOOK_STATUS\x10\x02\x12\x13\n\x0fUPDATE_PLAYBOOK\x10\x03\x12,\n(UPDATE_PLAYBOOK_ALERT_OPS_TRIGGER_STATUS\x10\x04\x42\x08\n\x06update*b\n\x1b\x45valuationConditionFunction\x12\x0f\n\x0bUNKNOWN_ECF\x10\x00\x12\x0b\n\x07\x45\x43\x46_AVG\x10\x01\x12\x0b\n\x07\x45\x43\x46_SUM\x10\x02\x12\x0b\n\x07\x45\x43\x46_MIN\x10\x03\x12\x0b\n\x07\x45\x43\x46_MAX\x10\x04*\x96\x01\n\x1b\x45valuationConditionOperator\x12\x0f\n\x0bUNKNOWN_ECO\x10\x00\x12\x10\n\x0cGREATER_THAN\x10\x01\x12\r\n\tLESS_THAN\x10\x02\x12\x16\n\x12GREATER_THAN_EQUAL\x10\x03\x12\x13\n\x0fLESS_THAN_EQUAL\x10\x04\x12\t\n\x05\x45QUAL\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06*_\n\x15PlaybookRunStatusType\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.playbook_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVALUATIONCONDITIONFUNCTION._serialized_start=15221
  _EVALUATIONCONDITIONFUNCTION._serialized_end=15319
  _EVALUATIONCONDITIONOPERATOR._serialized_start=15322
  _EVALUATIONCONDITIONOPERATOR._serialized_end=15472
  _PLAYBOOKRUNSTATUSTYPE._serialized_start=15474
  _PLAYBOOKRUNSTATUSTYPE._serialized_end=15569
  _PLAYBOOKMETRICTASKEXECUTIONRESULT._serialized_start=116
  _PLAYBOOKMETRICTASKEXECUTIONRESULT._serialized_end=1767
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT._serialized_start=416
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT._serialized_end=1767
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_GROUPBYLABELVALUE._serialized_start=694
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_GROUPBYLABELVALUE._serialized_end=802
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TIMESERIES._serialized_start=805
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TIMESERIES._serialized_end=1329
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TIMESERIES_LABELEDMETRICTIMESERIES._serialized_start=951
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TIMESERIES_LABELEDMETRICTIMESERIES._serialized_end=1329
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TIMESERIES_LABELEDMETRICTIMESERIES_DATAPOINT._serialized_start=1254
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TIMESERIES_LABELEDMETRICTIMESERIES_DATAPOINT._serialized_end=1329
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TABLERESULT._serialized_start=1332
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TABLERESULT._serialized_end=1702
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLECOLUMN._serialized_start=1443
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLECOLUMN._serialized_end=1589
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLEROW._serialized_start=1591
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLEROW._serialized_end=1702
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TYPE._serialized_start=1704
  _PLAYBOOKMETRICTASKEXECUTIONRESULT_RESULT_TYPE._serialized_end=1757
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT._serialized_start=1770
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT._serialized_end=2726
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT._serialized_start=2002
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT._serialized_end=2726
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT_ELSEEVALUATION._serialized_start=2382
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT_ELSEEVALUATION._serialized_end=2446
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT_TIMESERIESEVALUATION._serialized_start=2449
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT_TIMESERIESEVALUATION._serialized_end=2627
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT_TYPE._serialized_start=2629
  _PLAYBOOKDECISIONTASKEXECUTIONRESULT_RESULT_TYPE._serialized_end=2716
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT._serialized_start=2729
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT._serialized_end=3854
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT._serialized_start=3046
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT._serialized_end=3854
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TABLERESULT._serialized_start=3238
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TABLERESULT._serialized_end=3805
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLECOLUMN._serialized_start=1443
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLECOLUMN._serialized_end=1589
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLEROW._serialized_start=3691
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TABLERESULT_TABLEROW._serialized_end=3805
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TYPE._serialized_start=3807
  _PLAYBOOKDATAFETCHTASKEXECUTIONRESULT_RESULT_TYPE._serialized_end=3844
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT._serialized_start=3857
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT._serialized_end=4414
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT_RESULT._serialized_start=4109
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT_RESULT._serialized_end=4414
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT_RESULT_MARKDOWNRESULT._serialized_start=4314
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT_RESULT_MARKDOWNRESULT._serialized_end=4369
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT_RESULT_TYPE._serialized_start=4371
  _PLAYBOOKDOCUMENTATIONTASKEXECUTIONRESULT_RESULT_TYPE._serialized_end=4404
  _PLAYBOOKTASKEXECUTIONRESULT._serialized_start=4417
  _PLAYBOOKTASKEXECUTIONRESULT._serialized_end=4898
  _PLAYBOOKCLOUDWATCHTASK._serialized_start=4901
  _PLAYBOOKCLOUDWATCHTASK._serialized_end=5954
  _PLAYBOOKCLOUDWATCHTASK_CLOUDWATCHMETRICEXECUTIONTASK._serialized_start=5204
  _PLAYBOOKCLOUDWATCHTASK_CLOUDWATCHMETRICEXECUTIONTASK._serialized_end=5690
  _PLAYBOOKCLOUDWATCHTASK_CLOUDWATCHMETRICEXECUTIONTASK_DIMENSION._serialized_start=5590
  _PLAYBOOKCLOUDWATCHTASK_CLOUDWATCHMETRICEXECUTIONTASK_DIMENSION._serialized_end=5690
  _PLAYBOOKCLOUDWATCHTASK_CLOUDWATCHFILTERLOGEVENTSTASK._serialized_start=5693
  _PLAYBOOKCLOUDWATCHTASK_CLOUDWATCHFILTERLOGEVENTSTASK._serialized_end=5876
  _PLAYBOOKCLOUDWATCHTASK_TASKTYPE._serialized_start=5878
  _PLAYBOOKCLOUDWATCHTASK_TASKTYPE._serialized_end=5946
  _PLAYBOOKGRAFANATASK._serialized_start=5957
  _PLAYBOOKGRAFANATASK._serialized_end=6889
  _PLAYBOOKGRAFANATASK_PROMQLMETRICEXECUTIONTASK._serialized_start=6202
  _PLAYBOOKGRAFANATASK_PROMQLMETRICEXECUTIONTASK._serialized_end=6827
  _PLAYBOOKGRAFANATASK_PROMQLMETRICEXECUTIONTASK_LABELVALUE._serialized_start=6726
  _PLAYBOOKGRAFANATASK_PROMQLMETRICEXECUTIONTASK_LABELVALUE._serialized_end=6827
  _PLAYBOOKGRAFANATASK_TASKTYPE._serialized_start=6829
  _PLAYBOOKGRAFANATASK_TASKTYPE._serialized_end=6881
  _PLAYBOOKNEWRELICTASK._serialized_start=6892
  _PLAYBOOKNEWRELICTASK._serialized_end=8747
  _PLAYBOOKNEWRELICTASK_ENTITYAPPLICATIONGOLDENMETRICEXECUTIONTASK._serialized_start=7373
  _PLAYBOOKNEWRELICTASK_ENTITYAPPLICATIONGOLDENMETRICEXECUTIONTASK._serialized_end=7784
  _PLAYBOOKNEWRELICTASK_ENTITYDASHBOARDWIDGETNRQLMETRICEXECUTIONTASK._serialized_start=7787
  _PLAYBOOKNEWRELICTASK_ENTITYDASHBOARDWIDGETNRQLMETRICEXECUTIONTASK._serialized_end=8353
  _PLAYBOOKNEWRELICTASK_NRQLMETRICEXECUTIONTASK._serialized_start=8356
  _PLAYBOOKNEWRELICTASK_NRQLMETRICEXECUTIONTASK._serialized_end=8587
  _PLAYBOOKNEWRELICTASK_TASKTYPE._serialized_start=8590
  _PLAYBOOKNEWRELICTASK_TASKTYPE._serialized_end=8739
  _PLAYBOOKDATADOGTASK._serialized_start=8750
  _PLAYBOOKDATADOGTASK._serialized_end=9297
  _PLAYBOOKDATADOGTASK_SERVICEMETRICEXECUTIONTASK._serialized_start=8943
  _PLAYBOOKDATADOGTASK_SERVICEMETRICEXECUTIONTASK._serialized_end=9234
  _PLAYBOOKDATADOGTASK_TASKTYPE._serialized_start=9236
  _PLAYBOOKDATADOGTASK_TASKTYPE._serialized_end=9289
  _PLAYBOOKMETRICTASKDEFINITION._serialized_start=9300
  _PLAYBOOKMETRICTASKDEFINITION._serialized_end=9767
  _PLAYBOOKMETRICTASKDEFINITION_SOURCE._serialized_start=9664
  _PLAYBOOKMETRICTASKDEFINITION_SOURCE._serialized_end=9759
  _TIMESERIESEVALUATIONTASK._serialized_start=9770
  _TIMESERIESEVALUATIONTASK._serialized_end=10585
  _TIMESERIESEVALUATIONTASK_RULE._serialized_start=10025
  _TIMESERIESEVALUATIONTASK_RULE._serialized_end=10527
  _TIMESERIESEVALUATIONTASK_RULE_TYPE._serialized_start=10475
  _TIMESERIESEVALUATIONTASK_RULE_TYPE._serialized_end=10527
  _TIMESERIESEVALUATIONTASK_INPUTTYPE._serialized_start=10529
  _TIMESERIESEVALUATIONTASK_INPUTTYPE._serialized_end=10576
  _ELSEEVALUATIONTASK._serialized_start=10587
  _ELSEEVALUATIONTASK._serialized_end=10656
  _PLAYBOOKDOCUMENTATIONTASKDEFINITION._serialized_start=10659
  _PLAYBOOKDOCUMENTATIONTASKDEFINITION._serialized_end=10858
  _PLAYBOOKDOCUMENTATIONTASKDEFINITION_TYPE._serialized_start=4371
  _PLAYBOOKDOCUMENTATIONTASKDEFINITION_TYPE._serialized_end=4404
  _PLAYBOOKDECISIONTASKDEFINITION._serialized_start=10861
  _PLAYBOOKDECISIONTASKDEFINITION._serialized_end=11208
  _PLAYBOOKDECISIONTASKDEFINITION_EVALUATIONTYPE._serialized_start=11137
  _PLAYBOOKDECISIONTASKDEFINITION_EVALUATIONTYPE._serialized_end=11195
  _PLAYBOOKCLICKHOUSEDATAFETCHTASK._serialized_start=11210
  _PLAYBOOKCLICKHOUSEDATAFETCHTASK._serialized_end=11336
  _PLAYBOOKPOSTGRESDATAFETCHTASK._serialized_start=11338
  _PLAYBOOKPOSTGRESDATAFETCHTASK._serialized_end=11462
  _PLAYBOOKEKSDATAFETCHTASK._serialized_start=11465
  _PLAYBOOKEKSDATAFETCHTASK._serialized_end=11859
  _PLAYBOOKEKSDATAFETCHTASK_COMMANDTYPE._serialized_start=11764
  _PLAYBOOKEKSDATAFETCHTASK_COMMANDTYPE._serialized_end=11859
  _PLAYBOOKDATAFETCHTASKDEFINITION._serialized_start=11862
  _PLAYBOOKDATAFETCHTASKDEFINITION._serialized_end=12434
  _PLAYBOOKDATAFETCHTASKDEFINITION_SOURCE._serialized_start=12366
  _PLAYBOOKDATAFETCHTASKDEFINITION_SOURCE._serialized_end=12426
  _PLAYBOOKTASKDEFINITION._serialized_start=12437
  _PLAYBOOKTASKDEFINITION._serialized_end=13157
  _PLAYBOOKTASKDEFINITION_TYPE._serialized_start=13069
  _PLAYBOOKTASKDEFINITION_TYPE._serialized_end=13149
  _PLAYBOOKSTEPDEFINITION._serialized_start=13160
  _PLAYBOOKSTEPDEFINITION._serialized_end=13560
  _PLAYBOOKSTEPDEFINITION_EXTERNALLINK._serialized_start=13459
  _PLAYBOOKSTEPDEFINITION_EXTERNALLINK._serialized_end=13560
  _PLAYBOOK._serialized_start=13563
  _PLAYBOOK._serialized_end=14015
  _PLAYBOOKRUNLOG._serialized_start=14017
  _PLAYBOOKRUNLOG._serialized_end=14102
  _PLAYBOOKRUN._serialized_start=14105
  _PLAYBOOKRUN._serialized_end=14268
  _UPDATEPLAYBOOKOP._serialized_start=14271
  _UPDATEPLAYBOOKOP._serialized_end=15219
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOKNAME._serialized_start=14722
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOKNAME._serialized_end=14786
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOKSTATUS._serialized_start=14788
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOKSTATUS._serialized_end=14857
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOK._serialized_start=14859
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOK._serialized_end=14921
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOKALERTOPSTRIGGERSTATUS._serialized_start=14924
  _UPDATEPLAYBOOKOP_UPDATEPLAYBOOKALERTOPSTRIGGERSTATUS._serialized_end=15068
  _UPDATEPLAYBOOKOP_OP._serialized_start=15071
  _UPDATEPLAYBOOKOP_OP._serialized_end=15209
# @@protoc_insertion_point(module_scope)
