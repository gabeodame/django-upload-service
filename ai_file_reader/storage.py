# ai_file_reader/storage.py
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class TemporaryFileStorage(FileSystemStorage):
    """Store files in a temporary directory."""
    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.TEMP_MEDIA_ROOT
        super().__init__(*args, **kwargs)
