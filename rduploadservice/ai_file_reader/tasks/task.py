import os
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rduploadservice.ai_file_reader.storage import TemporaryFileStorage
from rduploadservice.ai_file_reader.tasks import process_uploaded_files_task

# Initialize temporary file storage
temp_storage = TemporaryFileStorage()


@csrf_exempt
def process_files(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    if 'files' not in request.FILES:
        return JsonResponse({'error': 'No files provided'}, status=400)

    uploaded_files = request.FILES.getlist('files')
    if not uploaded_files:
        return JsonResponse({'error': 'Empty file list'}, status=400)

    saved_file_paths = []
    try:
        # Save uploaded files temporarily
        for uploaded_file in uploaded_files:
            file_name = temp_storage.save(uploaded_file.name, uploaded_file)
            file_path = temp_storage.path(file_name)
            saved_file_paths.append(file_path)

        # Generate a unique task ID
        task_id = str(uuid.uuid4())

        # Dispatch the Celery task for asynchronous processing
        process_uploaded_files_task.delay(saved_file_paths, task_id)

        # Respond immediately with the task ID
        return JsonResponse({'task_id': task_id}, status=202)

    except Exception as e:
        # Clean up any saved files in case of an error
        for file_path in saved_file_paths:
            try:
                temp_storage.delete(file_path)
            except Exception as delete_error:
                # Log the deletion error if necessary
                pass

        return JsonResponse({'error': str(e)}, status=500)
