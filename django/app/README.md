### Запуск Django
(env) $ python3 manage.py runserver

### rabbitmq
$ docker-compose up

### Запуск rabbitmq
$ docker start rabbitmq

### Запуск celery
(env) $ celery -A blog worker -l info 

### Запуск celery beat
(env) $ celery -A blog beat -l info

### Запуск celery & celery-beat
(env) $ celery -A blog worker --beat --scheduler django --loglevel=info

### Запуск flower
(env) ~/.../app $ celery flower -A blog --address=127.0.0.1 --port=5555

