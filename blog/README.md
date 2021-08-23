## Блог содержащий статьи с разных сайтов

### Описание
-

### Запуск локально:

#### Django
(env) $ python3 manage.py runserver

#### rabbitmq
$ docker-compose up

#### Запуск rabbitmq
$ docker start rabbitmq

#### Запуск celery
(env) $ celery -A blog worker -l info 

#### Запуск celery beat
(env) $ celery -A blog beat -l info

#### Запуск celery & celery-beat
(env) $ celery -A blog worker --beat --scheduler django --loglevel=info

#### Запуск flower
(env) ~/.../app $ celery flower -A blog --address=127.0.0.1 --port=5555


### API

| Endpoint        | HTTP Method | Result                  |
|-----------------|-------------|-------------------------|
| article/api     | GET         | Get all articles        |
| article/api     | POST        | Add articles            |
| article/api/:id | GET         | Get a single article    |
| article/api/:id | PUT         | Update a single article |
| article/api/:id | DELETE      | Delete a single article |

### Реализованно
CRUD операции для работы со статьями. Есть endpoint для получения статей
(репозиторий MediaParser). 

### Планируется
* запуск парсинга статей (запрос на aiohttp сервер, репозиторий MediaParser)
* рассылать по расписанию / отображать статьи с новостных сайтов,
  по заданным ключевым словам (война, кризис и т.д.)
* настроить nginx, gunicorn, wsgi
* обернуть web-приложение в docker

