## Запуск Django
____

1) запуск rabbitmq
ivan@ivan-M5400:~/Git/blog/django/app$ docker-compose start
или
docker start [rabbitmq]

2) запуск celery / celery beat
(env) ivan@ivan-M5400:~/Git/blog/django/app$ celery -A blog worker --beat --scheduler django --loglevel=info

