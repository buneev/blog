FROM alpine:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add --no-cache \
        uwsgi-python3 \
        python3

RUN pip3 install --upgrade pip
RUN pip3 install uwsgi

RUN mkdir /code
WORKDIR /code

# install psycopg2 dependencies
RUN apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install uwsgi
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

RUN chmod +x run_celery.sh
RUN chmod +x run_django.sh

