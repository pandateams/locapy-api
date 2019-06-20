# -*- coding: utf-8 -*-

import os

from celery import Celery
from raven.contrib.celery import register_signal
from raven.contrib.django.raven_compat.models import client as client_raven

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locapy.settings.base")

app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

register_signal(client_raven)
