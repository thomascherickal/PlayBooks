from typing import Dict

from google.protobuf.wrappers_pb2 import StringValue, UInt64Value
from connectors.models import Connector, ConnectorKey
from executor.playbook_task_executor import PlaybookTaskExecutor
from integrations_api_processors.db_connection_string_processor import DBConnectionStringProcessor
from protos.base_pb2 import Source, SourceKeyType, TimeRange
from protos.playbooks.playbook_commons_pb2 import PlaybookTaskResult, TableResult, PlaybookTaskResultType
from protos.playbooks.playbook_v2_pb2 import PlaybookTask


class SqlDatabaseConnectionTaskExecutor(PlaybookTaskExecutor):

    def __init__(self, account_id):
        self.source = Source.SQL_DATABASE_CONNECTION

        self.__account_id = account_id

        try:
            sql_database_connector = Connector.objects.get(account_id=account_id,
                                                           connector_type=Source.SQL_DATABASE_CONNECTION,
                                                           is_active=True)
        except Connector.DoesNotExist:
            raise Exception("Active SQL Database connector not found for account: {}".format(account_id))
        if not sql_database_connector:
            raise Exception("Active SQL Database connector not found for account: {}".format(account_id))

        sql_database_connector_keys = ConnectorKey.objects.filter(connector_id=sql_database_connector.id,
                                                                  account_id=account_id,
                                                                  is_active=True)
        if not sql_database_connector_keys:
            raise Exception("Active SQL Database connector keys not found for account: {}".format(account_id))

        for key in sql_database_connector_keys:
            if key.key_type == SourceKeyType.SQL_DATABASE_CONNECTION_STRING_URI:
                self.__connection_string = key.key

        if not self.__connection_string:
            raise Exception("SQL Database connection string not found for account: {}".format(account_id))

        try:
            self.client = DBConnectionStringProcessor(self.__connection_string)
            self.client.test_connection()
        except Exception as e:
            raise Exception(f"Error while connecting to SQL Database: {e}")

    def execute(self, time_range: TimeRange, global_variable_set: Dict, task: PlaybookTask) -> PlaybookTaskResult:
        try:
            sql_database_connection_data_fetch_task = task.sql_database_connection_data_fetch_task
            order_by_column = sql_database_connection_data_fetch_task.order_by_column.value
            limit = sql_database_connection_data_fetch_task.limit.value
            offset = sql_database_connection_data_fetch_task.offset.value
            query = sql_database_connection_data_fetch_task.query.value
            query = query.strip()
            if query[-1] == ';':
                query = query[:-1]
            for key, value in global_variable_set.items():
                query = query.replace(key, str(value))
            count_query = f"SELECT COUNT(*) FROM ({query}) AS subquery"
            if order_by_column and 'order by' not in query.lower():
                query = f"{query} ORDER BY {order_by_column} DESC"
            if limit and offset and 'limit' not in query.lower():
                query = f"{query} LIMIT {limit} OFFSET {offset}"
            if not limit and 'limit' not in query.lower():
                limit = 10
                offset = 0
                query = f"{query} LIMIT 2000 OFFSET 0"

            count_result = self.client.get_query_result(count_query).fetchone()[0]

            print("Playbook Task Downstream Request: Type -> {}, Account -> {}, Query -> {}".format(
                "SQL Database", self.__account_id, query), flush=True)

            query_result = self.client.get_query_result(query).fetchall()

            table_rows: [TableResult.TableRow] = []
            col_names = list(self.client.get_query_result(query).keys())
            for row in query_result:
                table_columns = []
                for i, value in enumerate(row):
                    table_column = TableResult.TableColumn(name=StringValue(value=col_names[i]),
                                                           value=StringValue(value=str(value)))
                    table_columns.append(table_column)
                table_rows.append(TableResult.TableRow(columns=table_columns))
            table = TableResult(raw_query=sql_database_connection_data_fetch_task.query,
                                total_count=UInt64Value(value=int(count_result)),
                                limit=UInt64Value(value=limit),
                                offset=UInt64Value(value=offset),
                                rows=table_rows)
            return PlaybookTaskResult(type=PlaybookTaskResultType.TABLE, table=table, source=self.source)
        except Exception as e:
            raise Exception(f"Error while executing Sql Database task: {e}")
