#!/bin/sh

# wait for PSQL server to start
sleep 5

cd app
# prepare init migration
python manage.py makemigrations myproject
# migrate db, so we have the latest db schema
python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
gunicorn blog.wsgi:application --bind=0.0.0.0:8000 --workers=4 --timeout=300
