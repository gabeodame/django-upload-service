from django.http import JsonResponse
from celery.result import AsyncResult
from django.views.decorators.http import require_GET

@require_GET
def task_status_view(request, task_id):
    result = AsyncResult(task_id)

    payload = {
        'task_id': task_id,
        'status': result.status,
    }

    if result.successful():
        payload['result'] = result.result
    elif result.failed():
        payload['error'] = str(result.result)

    return JsonResponse(payload)
