from django.db import models
from django.conf import settings

class SiteUser(models.Model):
	"""Wraps a User model to facilitate extra fields.

	Example usage: profile pictures, user bios, etc.

	Access the Django User object using the equiv_user field.
	"""
	equiv_user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		verbose_name="related internal user object",
		related_name="site_user",
	)
