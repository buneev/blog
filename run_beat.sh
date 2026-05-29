#!/bin/sh

sleep 5

cd app
rm -f celerybeat.pid
celery -A blog beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
