# Create your tasks here
from __future__ import absolute_import, unicode_literals

from time import sleep
from celery import shared_task

@shared_task(name="hello_world")
def hello_world():
    sleep(10) # поставим задержку 10с для демонстрации асинхронности
    print('Hello World task')
    return 'Task completed successfully'

@shared_task()
def add(x=3, y=7):
    print('Add 2 numbers task')
    return x + y

# @app.task(bind=True, default_retry_delay=30 * 60)  # retry in 30 minutes.
# def add(self, x, y):
#     try:
#         something_raising()
#     except Exception as exc:
#         # overrides the default delay to retry after 1 minute
#         raise self.retry(exc=exc, countdown=60)
