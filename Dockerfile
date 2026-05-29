FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN grep -v "^uWSGI" requirements.txt > req_no_uwsgi.txt && \
    pip install --no-cache-dir --default-timeout=120 -r req_no_uwsgi.txt

COPY . .

RUN chmod +x run_django.sh run_celery.sh run_beat.sh

CMD ["./run_django.sh"]
