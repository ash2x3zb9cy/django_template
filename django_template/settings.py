import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# def path(*paths):
#     return os.path.join(BASE_DIR, *paths)

from .conf.i18n import *
from .conf.staticfiles import *
from .conf.auth import *
from .conf.hosting import *
from .conf.templates import *
from .conf.apps import *

if os.environ.get('PRODUCTION', '').lower() == 'true':
    from .conf.production import *
else:
    from .conf.debug import *
