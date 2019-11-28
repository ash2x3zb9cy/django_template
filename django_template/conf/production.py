import os

try:
	SECRET_KEY = os.environ['SECRET_KEY']
except KeyError as e:
	raise EnvironmentError('SECRET_KEY environment variable needs to be set in production', e)

# just in case
Debug = False

# configure this with the domain you are hosting on.
ALLOWED_HOSTS = []

# Read the docs before enabling this.
# SECURE_HSTS_SECONDS = ??????
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Need SSL!
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
