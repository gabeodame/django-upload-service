from datetime import datetime
from io import BytesIO
import json
from typing import Dict, Any, List, Union
from django.shortcuts import render
import jwt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from django.conf import settings

from uploadservice.backends import WindowsAuthenticationBackend
from .serializers import FileSerializer
from .models import UploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
import os
import logging

logger = logging.getLogger(__name__)

def index(request):
    print(request)
    return render(request, 'uploadservice/index.html')

def cors_preflight_view(request):
    response = JsonResponse({'detail': 'CORS Preflight'})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


#IIS Debug
def print_meta(request):
    def serialize_meta_value(value):
        if isinstance(value, bytes):
            return value.decode('utf-8', errors='ignore')
        elif isinstance(value, BytesIO):
            return value.getvalue().decode('utf-8', errors='ignore')
        else:
            try:
                json.dumps(value)
                return value
            except (TypeError, OverflowError):
                return str(value)

    meta_dict = {k: serialize_meta_value(v) for k, v in request.META.items()}
    
    # Write meta_dict to a file
    with open('meta_info.json', 'w') as f:
        json.dump(meta_dict, f, indent=4)
    
    return JsonResponse(meta_dict)

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    

    def post(self, request: HttpRequest, folder: str, brand_name: str, kind: str, date: str = '') -> JsonResponse:
        if not request.FILES:
            return JsonResponse({"error": "No files uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_files_info: List[Dict[str, Any]] = []

        for key, uploaded_file in request.FILES.items():
            original_filename = uploaded_file.name
            file_basename, file_extension = os.path.splitext(original_filename)

            base_path = os.path.join(settings.MEDIA_ROOT, 'chemicalUploads')
            if kind == "sdsFile":
                folder_path = os.path.join(base_path, folder, 'sds')
                file_name = f"{file_basename}_{brand_name}_{date or ''}{file_extension}"
            elif kind == "coaFile":
                folder_path = os.path.join(base_path, folder, 'coa')
                file_name = f"{file_basename}_{brand_name}{file_extension}"
            else:
                folder_path = os.path.join(base_path, folder, 'other-files')
                file_name = f"{file_basename}_{brand_name}{file_extension}"

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_path = os.path.join(folder_path, file_name)
            default_storage.save(file_path, ContentFile(uploaded_file.read()))

            # Save file details to the database, including the file path
            uploaded_file_record = UploadedFile(
                folder=folder,
                brand_name=brand_name,
                date=date or '',  # Handle optional date
                kind=kind,
                file_name=file_name,
                filepath=file_path  # Save the file path
            )
            uploaded_file_record.save()

            uploaded_files_info.append({
                "uploaded_file_id": uploaded_file_record.id,
                "file_path": uploaded_file_record.filepath
            })

        return JsonResponse({
            "message": "Files uploaded successfully",
            "uploaded_files": uploaded_files_info
        }, status=status.HTTP_201_CREATED)
      

class LoginView(APIView):
    def post(self, request: HttpRequest) -> JsonResponse:
        user = authenticate(request, remote_user=request.META.get('REMOTE_USER'))
        if user is not None and isinstance(user, User):
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token # type: ignore
            
            logger.info(access_token)
            print(access_token)

            return JsonResponse({
                'refresh': str(refresh),
                'access': str(access_token),
                'username': user.username,
                'full_name': f'{user.first_name} {user.last_name}',
                'email': user.email,
            })
        else:
            return JsonResponse({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

class ObtainJWTView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        user = authenticate(request, remote_user=username)  # Use Windows Authentication

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token # type: ignore
            
            logger.info(access_token)
            print(access_token)

            return Response({
                'refresh': str(refresh),
                'access': str(access_token),
                'username': user.username, # type: ignore
                'full_name': f'{user.first_name} {user.last_name}', # type: ignore
                'email': user.email, # type: ignore
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
