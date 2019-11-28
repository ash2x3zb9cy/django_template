from django.test import TestCase
from django.contrib.auth.models import User
from .backends import CaseInsensitiveModelBackend
from .models import SiteUser

class CaseInsensitiveModelBackendTest(TestCase):
	def setUp(self):
		user = User.objects.create_user('Username1', 'AaBb@domain.tld', 'pip install Django=2.2', pk=1)
		site_user = SiteUser.objects.create(equiv_user=user)
		user.save()
		site_user.save()

	def try_login(self, username, password):
		return CaseInsensitiveModelBackend().authenticate(None, username, password)

	def test_exact_password_matches(self):
		"""Users can authenticate with case-exact usernames."""
		result = self.try_login('Username1', 'pip install Django=2.2')
		self.assertIsNotNone(result)

	def test_allcaps_password_matches(self):
		"""Users can authenticate with all-caps username entry."""
		result = self.try_login('USERNAME1', 'pip install Django=2.2')
		self.assertIsNotNone(result)

	def test_passwords_case_sensitive(self):
		"""Users cannot authenticate with non-case-exact passwords."""
		result = self.try_login('Username1', 'pip INSTALL django=2.2')
		self.assertIsNone(result)

	def test_nonexistent_users_dont_validate(self):
		"""Login attempts with invalid usernames fail."""
		result = self.try_login('username2', 'pip install Django=2.2')
		self.assertIsNone(result)
