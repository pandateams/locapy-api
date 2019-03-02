import django_heroku

from .base import *

DEBUG = False

ALLOWED_HOSTS = []

# Logging
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN'),
    'environment': 'prod',
}

# Activate Django-Heroku.
django_heroku.settings(locals())
