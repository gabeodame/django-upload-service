
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User
from .utils import get_user_info

class WindowsAuthenticationBackend(RemoteUserBackend):
    def authenticate(self, request, remote_user):
        if not remote_user:
            return None

        user_info = get_user_info(remote_user)
        if not user_info:
            return None

        try:
            user = User.objects.get(username=remote_user)
        except User.DoesNotExist:
            # Optionally create a user if it does not exist
            user = User(username=remote_user, email=user_info['email'])
            user.set_unusable_password()
            user.save()

        # Update user information
        user.first_name = user_info['full_name'].split(' ')[0]
        user.last_name = ' '.join(user_info['full_name'].split(' ')[1:])
        user.email = user_info['email']
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
