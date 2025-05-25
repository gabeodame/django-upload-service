from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
from django.conf import settings

# /api/tasks/<task_id>/status/


@csrf_exempt
def task_status_view(request, task_id):
    try:
        task_result = AsyncResult(task_id)
        response = {
            'task_id': task_id,
            'status': task_result.status,
        }

        if task_result.status == 'SUCCESS':
            response['result'] = task_result.result

        elif task_result.status == 'FAILURE':
            response['error'] = str(task_result.result)

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
