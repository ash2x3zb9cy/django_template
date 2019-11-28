from django.contrib.auth.backends import ModelBackend

""" technically should be using settings.AUTH_USER_MODEL,
but that doesn't work with my IntelliSense thing
because of the way that settings works.
FIXME: change to AUTH_USER_MODEL
"""
from django.contrib.auth.models import User

class CaseInsensitiveModelBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None):
		try:
			user = User.objects.get(username__iexact=username)
			if user.check_password(password) and self.user_can_authenticate(user):
				return user
		except User.DoesNotExist:
			# apparently this can reduce timing attacks on users
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
