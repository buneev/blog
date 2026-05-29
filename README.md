## Блог содержащий статьи с разных сайтов

### Запуск локально:

#### 1. PostgreSQL 12

Установка (если ещё не установлен):
```bash
brew install postgresql@12
```

Запуск:
```bash
brew services start postgresql@12
```

Создание пользователя и базы данных:
```bash
createuser -s blog_user
createdb -O blog_user blog
```

Проверка подключения:
```bash
psql -U blog_user -h 127.0.0.1 -p 5432 -d blog
```
Пароль: `123456` (указан в `app/blog/.env`)

#### 2. Виртуальное окружение

Создание и активация:
```bash
python3.10 -m venv env
source env/bin/activate
```

Установка зависимостей:
```bash
pip install -r requirements.txt
```

#### 3. Django

Применить миграции:
```bash
python app/manage.py migrate
```

Запуск сервера:
```bash
python app/manage.py runserver
```

#### 4. RabbitMQ
```bash
docker-compose up
```

#### Запуск rabbitmq
```bash
docker start rabbitmq
```

#### Запуск celery
```bash
celery -A blog worker -l info
```

#### Запуск celery beat
```bash
celery -A blog beat -l info
```

#### Запуск celery & celery-beat
```bash
celery -A blog worker --beat --scheduler django --loglevel=info
```

#### Запуск flower
```bash
celery flower -A blog --address=127.0.0.1 --port=5555
```


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
  по заданным ключевым словам (погода, кризис и т.д.)
* настроить nginx, gunicorn, wsgi
* обернуть web-приложение в docker

