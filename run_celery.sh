#!/bin/sh

sleep 5

cd app
celery -A blog worker -l info