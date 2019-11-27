from .APP_NAME import APP_NAME

"""
WSGI config for {} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
""".format(APP_NAME)

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings'.format(APP_NAME))

application = get_wsgi_application()
