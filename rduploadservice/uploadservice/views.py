from io import BytesIO
import json
import mimetypes
from typing import Dict, Any, List, Union
from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser

from django.conf import settings
from .serializers import FileSerializer
from .models import UploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import User
import os

from django.contrib.auth import authenticate

def index(request):
    return render(request, 'uploadservice/index.html')

# Remove custom CORS headers from this view
def cors_preflight_view(request):
    response = JsonResponse({'detail': 'CORS Preflight'})
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

# file list view
def list_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'uploadservice/list_files.html', {'files': files})

#serve file by id
def serve_file(request, file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
    except UploadedFile.DoesNotExist:
        raise Http404("File not found")

    file_path = uploaded_file.filepath
    if not os.path.exists(file_path):
        raise Http404("File not found")

    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        mime_type = 'application/octet-stream'

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type=mime_type)
        response['Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
        return response

def get_file_details(request, file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
        file_data = {
            "id": uploaded_file.id,
            "folder": uploaded_file.folder,
            "brand_name": uploaded_file.brand_name,
            "date": uploaded_file.date,
            "kind": uploaded_file.kind,
            "file_name": uploaded_file.file_name,
            "filepath": uploaded_file.filepath,
            "upload_time": uploaded_file.upload_time,
        }
        return JsonResponse(file_data)
    except UploadedFile.DoesNotExist:
        return JsonResponse({"error": "File not found"}, status=404)

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [authenticate.is]

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
            access_token = refresh.token

            return JsonResponse({
                'refresh': str(refresh),
                'access': str(access_token),
                'username': user.username,
                'full_name': f'{user.first_name} {user.last_name}',
                'email': user.email,
            })
        else:
            return JsonResponse({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
