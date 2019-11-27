#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# FIXME: change this to the name of the dir containing settings.py!
APP_BASE_DIR = 'django_template'

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings'.format(APP_BASE_DIR))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
