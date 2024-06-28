from django.urls import path
from .views import FileUploadView, index, LoginView, ObtainJWTView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', index, name='home-page'),
    path('uploads/<str:folder>/<str:brand_name>/<str:kind>/', FileUploadView.as_view(), name='file-upload-without-date'),
    path('uploads/<str:folder>/<str:brand_name>/<str:date>/<str:kind>/', FileUploadView.as_view(), name='file-upload'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api-token-auth/', ObtainJWTView.as_view(), name='api-token-auth'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]