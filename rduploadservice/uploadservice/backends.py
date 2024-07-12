# backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class WindowsAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Use REMOTE_USER header set by IIS
        remote_user = request.META.get('REMOTE_USER')

        if not remote_user:
            return None

        # Extract username
        username = remote_user.split('\\')[-1]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.set_unusable_password()
            user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
