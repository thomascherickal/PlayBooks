export const taskTypes = {
  CLOUDWATCH_METRIC: "CLOUDWATCH METRIC_EXECUTION",
  CLOUDWATCH_LOG_GROUP: "CLOUDWATCH FILTER_LOG_EVENTS",
  EKS_GET_PODS: "EKS GET_PODS",
  EKS_GET_DEPLOYMENTS: "EKS GET_DEPLOYMENTS",
  EKS_GET_EVENTS: "EKS GET_EVENTS",
  EKS_GET_SERVICES: "EKS GET_SERVICES",
  DATADOG_SERVICE_METRIC_EXECUTION: "DATADOG SERVICE_METRIC_EXECUTION",
  DATADOG_QUERY_METRIC_EXECUTION: "DATADOG QUERY_METRIC_EXECUTION",
  NEW_RELIC_ENTITY_APPLICATION_GOLDEN_METRIC_EXECUTION:
    "NEW_RELIC ENTITY_APPLICATION_GOLDEN_METRIC_EXECUTION",
  NEW_RELIC_ENTITY_DASHBOARD_WIDGET_NRQL_METRIC_EXECUTION:
    "NEW_RELIC ENTITY_DASHBOARD_WIDGET_NRQL_METRIC_EXECUTION",
  NEW_RELIC_NRQL_METRIC_EXECUTION: "NEW_RELIC NRQL_METRIC_EXECUTION",
  GRAFANA_PROMQL_METRIC_EXECUTION: "GRAFANA PROMQL_METRIC_EXECUTION",
  GRAFANA_PROMETHEUS_DATASOURCE:
    "GRAFANA PROMETHEUS_DATASOURCE_METRIC_EXECUTION",
  GRAFANA_VPC_PROMQL_METRIC_EXECUTION: "GRAFANA_VPC PROMQL_METRIC_EXECUTION",
  GRAFANA_MIMIR_PROMQL_METRIC_EXECUTION:
    "GRAFANA_MIMIR PROMQL_METRIC_EXECUTION",
  AZURE_FILTER_LOG_EVENTS: "AZURE FILTER_LOG_EVENTS",
  POSTGRES_SQL_QUERY: "POSTGRES SQL_QUERY",
  CLICKHOUSE_SQL_QUERY: "CLICKHOUSE SQL_QUERY",
  SQL_DATABASE_CONNECTION_SQL_QUERY: "SQL_DATABASE_CONNECTION SQL_QUERY",
  API_HTTP_REQUEST: "API HTTP_REQUEST",
  BASH_COMMAND: "BASH COMMAND",
  DOCUMENTATION_MARKDOWN: "DOCUMENTATION MARKDOWN",
  DOCUMENTATION_IFRAME: "DOCUMENTATION IFRAME",
};
