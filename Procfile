web: gunicorn locapy.wsgi --log-file -
worker: celery -A locapy worker -l INFO
beat: celery -A locapy beat --pidfile=/tmp/celery-beat.pid -l INFO