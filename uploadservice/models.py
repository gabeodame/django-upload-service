# models.py

from django.db import models

class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    folder = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    date = models.CharField(max_length=255, blank=True, null=True)  # Allow date to be optional
    kind = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    filepath = models.CharField(max_length=1024)  # Save the full file path
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
