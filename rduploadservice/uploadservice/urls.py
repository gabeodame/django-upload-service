from django.urls import path
from .views import (
    FileListApiView, index, list_files, serve_file, get_file_details,
    SDSUploadView, COAUploadView, OtherUploadView,
    LoginView
)

urlpatterns = [
    path('', index, name='home-page'),
    path('files/', list_files, name='list_files'),
    path('files/<int:file_id>/', serve_file, name='serve_file'),
    path('files/details/<int:file_id>/', get_file_details, name='get_file_details'),

    # upload endpoints
    path('api/uploads/sds/<str:folder>/<path:brand_name>/<str:date>/', SDSUploadView.as_view(), name='upload-sds'),
    path('api/uploads/coa/<str:folder>/<path:brand_name>/', COAUploadView.as_view(), name='upload-coa'),
    path('api/uploads/other/<str:folder>/<path:brand_name>/', OtherUploadView.as_view(), name='upload-other'),
    path('api/files/', FileListApiView.as_view(), name='api-list-files'),

    # Login endpoint
    path('api/login/', LoginView.as_view(), name='login'),
]
