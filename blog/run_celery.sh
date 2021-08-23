#!/bin/sh

# wait for RabbitMQ server to start
sleep 5

cd app
# run celery & celery-beat 
celery -A blog worker --beat --scheduler django --loglevel=info # -Q default