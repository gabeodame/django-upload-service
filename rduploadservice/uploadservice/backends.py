from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User
from django.db import transaction
import logging
import jwt
from django.conf import settings
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class WindowsAuthenticationBackend(RemoteUserBackend):
    def authenticate(self, request, remote_user=None):
        if not remote_user:
            return None

        # Log the attempt
        logger.info(f"Attempting to authenticate user: {remote_user}")

        # Split the domain and username
        try:
            domain, username = remote_user.split('\\')
        except ValueError:
            logger.error(f"Failed to split domain and username for remote_user: {remote_user}")
            return None

        # Get user information from a custom function
        user_info = self.get_user_info(username)
        if not user_info:
            logger.error(f"Failed to retrieve user info for {username}")
            return None

        try:
            with transaction.atomic():
                user, created = User.objects.get_or_create(username=username)
                if created:
                    logger.info(f"Created new user: {username}")

                # Update user information
                user.first_name = user_info.get('first_name', '')
                user.last_name = user_info.get('last_name', '')
                user.email = user_info.get('email', '')
                user.set_unusable_password()
                user.save()

                logger.info(f"Updated user info for: {username}")
        except Exception as e:
            logger.error(f"Error authenticating user {username}: {e}")
            return None

        return user

    def get_user_info(self, username):
        # Implement a way to get additional user info (e.g., from a database, API, or file)
        user_info = {}
        try:
            # Replace this with actual logic to fetch user details
            user_info = {
                'first_name': 'FirstName',  # Placeholder
                'last_name': 'LastName',  # Placeholder
                'email': f'{username}@example.com'  # Placeholder
            }
        except Exception as e:
            logger.error(f'Error retrieving user info for {username}: {e}')
        return user_info

    def generate_jwt_token(self, user):
        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.utcnow() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
