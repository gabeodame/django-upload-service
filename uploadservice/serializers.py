# serializers.py

from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'
        read_only_fields = ('folder', 'brand_name', 'date', 'kind', 'file_name')

class UploadedFileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ['id', 'folder', 'brand_name', 'date', 'kind', 'file_name', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/files/{obj.id}")
        return f"/files/{obj.id}"  # fallback