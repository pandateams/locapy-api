from dj_database_url import parse as dburl

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# !!!! BANCO DOCKER !!!!
DATABASES = {
    'default': dburl(config('DOCKER_DATABASE'), conn_max_age=600),
}

# Logging
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN'),
    'environment': 'dev',
}
