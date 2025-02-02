from django.conf import settings
from django.urls import path

from . import views as workflow_views

urlpatterns = [

    # CRUD
    path('get', workflow_views.workflows_get),
    path('create', workflow_views.workflows_create),
    path('update', workflow_views.workflows_update),

    # Execution APIs
    path('execute', workflow_views.workflows_execute),
    path('executions/get', workflow_views.workflows_execution_get),  # deprecated
    path('executions/get/v2', workflow_views.workflows_execution_get_v2),
    path('executions/list', workflow_views.workflows_execution_list),

    # API based executions
    path(settings.WORKFLOW_EXECUTE_API_PATH, workflow_views.workflows_api_execute),
    path(settings.WORKFLOW_EXECUTIONS_GET_API_PATH, workflow_views.workflows_execution_api_get),  # deprecated
    path(settings.WORKFLOW_EXECUTIONS_GET_API_PATH_V2, workflow_views.workflows_execution_api_get_v2),

    # Platform APIs
    path('test_notification', workflow_views.test_workflows_notification),
    path('generate/curl', workflow_views.generate_curl),

]
