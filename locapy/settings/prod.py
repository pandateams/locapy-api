from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Logging
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN'),
    'environment': 'prod',
}

# Como estamos usando a conta gratuita do Heroku, só podemos utilizar 3 conexões no maximo
BROKER_POOL_LIMIT = 3
