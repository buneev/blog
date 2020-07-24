from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    # Executes every 30 minutes
    'mul_2_numbers': {
        'task': 'article.tasks.mul_2_numbers',
        'schedule': crontab(minute="*/30"),
        'args': (7, 20),
    },
}
app.conf.timezone = 'UTC'