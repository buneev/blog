# Create your tasks here
from __future__ import absolute_import, unicode_literals

from time import sleep
from celery import shared_task

@shared_task()
def mul_2_numbers(x=3, y=7):
    sleep(10)
    print('Mul 2 numbers task')
    return x * y

@shared_task(name="hello_world")
def hello_world():
    sleep(10) # поставим тут задержку в 10 сек для демонстрации ассинхрности
    print('Hello World task')
    return 'Task completed successfully'