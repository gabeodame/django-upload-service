from .celery import app as celery_app

# Celery CLI expects an attribute named "celery" in some setups.
celery = celery_app

__all__ = ("celery_app",)
