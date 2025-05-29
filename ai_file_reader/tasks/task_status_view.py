from django.http import JsonResponse
from celery.result import AsyncResult
from django.views.decorators.http import require_GET

@require_GET
def task_status_view(request, task_id):
    result = AsyncResult(task_id)

    return JsonResponse({
        'task_id': task_id,
        'status': result.status,
        'result': result.result if result.ready() else None
    })
