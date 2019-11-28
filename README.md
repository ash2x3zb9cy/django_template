# django_template

a Django project with some opinionated defaults.

## Usage

### Renaming the app

There are three places the app's name is written:

- main app directory name
- `APP_BASE_DIR` in `manage.py`
- `APP_NAME` in `<APP_BASE_DIR>/APP_NAME.py`

In this template, these are set to 'django_template'. They need to all be set to the same value as each other.

### Template templates

This repository provides a basic template setup, with a base template located at `django_template/templates/base.html`. It has the following features:
- `body` block for main page content
- Nav bar
- Style provided by [bulma](https://bulma.io), via [CDN](https://www.jsdelivr.com/package/npm/bulma)
- `head` block for additional CSS/JS/etc
