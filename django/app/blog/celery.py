from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from .settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog', broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY') # переменные которые начинаются с CELERY
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
