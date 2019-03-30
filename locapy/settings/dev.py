from dj_database_url import parse as dburl

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# !!!! BANCO DOCKER !!!!
sqlite_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': dburl(config('DOCKER_DATABASE'), conn_max_age=600),
    'sqlite': dj_database_url.parse(sqlite_url, conn_max_age=600),
}

# Logging
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN'),
    'environment': 'dev',
}
