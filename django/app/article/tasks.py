# Create your tasks here
from __future__ import absolute_import, unicode_literals

from time import sleep
from celery import shared_task

@shared_task()
def mul_2_numbers(x=3, y=7):
    sleep(10)
    print('CALL MUL TASK')
    return x * y

