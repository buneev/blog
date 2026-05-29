#!/bin/sh

#!/bin/sh

sleep 5

cd app
python manage.py migrate
gunicorn blog.wsgi:application --bind=0.0.0.0:8000 --workers=4 --timeout=300
