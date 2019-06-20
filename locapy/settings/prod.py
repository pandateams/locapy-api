from .base import *
from locapy.celery import app

DEBUG = False

ALLOWED_HOSTS = ['*']

# Logging
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN'),
    'environment': 'prod',
}

# Como estamos usando a conta gratuita do Heroku, só podemos utilizar 3 conexões no maximo
BROKER_URL = config('CLOUDAMQP_URL')
BROKER_POOL_LIMIT = 3
BROKER_CONNECTION_MAX_RETRIES = None

app.conf.update(BROKER_URL=config('CLOUDAMQP_URL'))
