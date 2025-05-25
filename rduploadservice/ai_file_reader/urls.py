from django.urls import path
from .views import process_files
from tasks.task_status_view import task_status_view

urlpatterns = [
    path('process-files/', process_files, name='process_files'),
    path('api/tasks/<uuid:task_id>/status/',
         task_status_view, name='task_status'),
]
