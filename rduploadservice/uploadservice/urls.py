# urls.py

from django.urls import path
from .views import FileUploadView, get_file_details, index, LoginView, list_files, serve_file

urlpatterns = [
    path('', index, name='home-page'),
    path('files/', list_files, name='list_files'),
    path('files/<int:file_id>/', serve_file, name='serve_file'),
    path('files/details/<int:file_id>/', get_file_details, name='get_file_details'),
    path('uploads/<str:folder>/<str:brand_name>/<str:kind>/', FileUploadView.as_view(), name='file-upload-without-date'),
    path('uploads/<str:folder>/<str:brand_name>/<str:date>/<str:kind>/', FileUploadView.as_view(), name='file-upload'),
    path('api/login/', LoginView.as_view(), name='login'),
]
