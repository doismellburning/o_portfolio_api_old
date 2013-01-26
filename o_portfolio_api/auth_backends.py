import logging

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


logger = logging.getLogger('api')


class CustomUserModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        """Allow users to log in with their email as well as username."""
        # logger.info('username: {0}'.format(username))
        kw = 'email__iexact' if '@' in username else 'username'
        kwargs = {kw: username}
        try:
            user = User.objects.get(**kwargs)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user

