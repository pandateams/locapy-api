web: gunicorn --env DJANGO_SETTINGS_MODULE=locapy.settings.prod locapy.wsgi:application
worker: celery worker --beat --pidfile=/tmp/celery-beat.pid --loglevel=info