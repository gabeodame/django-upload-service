from django.urls import path
from .views import FileUploadView, index, LoginView

urlpatterns = [
    path('', index, name='home-page'),
     path('uploads/<str:folder>/<str:brand_name>/<str:kind>/', FileUploadView.as_view(), name='file-upload-without-date'),
    path('uploads/<str:folder>/<str:brand_name>/<str:date>/<str:kind>/', FileUploadView.as_view(), name='file-upload'),
     path('api/login/', LoginView.as_view(), name='login'),
]