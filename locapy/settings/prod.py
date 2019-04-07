from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Logging
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN'),
    'environment': 'prod',
}
