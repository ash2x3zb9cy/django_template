import os

from ..APP_NAME import APP_NAME

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def path(*paths):
    return os.path.join(BASE_DIR, *paths)

WSGI_APPLICATION = '{}.wsgi.application'.format(APP_NAME)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path('db.sqlite3'),
    }
}
