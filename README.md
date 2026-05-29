## Блог содержащий статьи с разных сайтов

### Запуск через Docker (рекомендуется)

Поднимает 5 сервисов: PostgreSQL, RabbitMQ, Django (gunicorn), Celery Worker, Celery Beat.
Один образ собирается и переиспользуется для всех сервисов приложения.

#### 1. Сборка образа

```bash
docker compose build
```

#### 2. Запуск всех сервисов

```bash
docker compose up
```

Django будет доступен на `http://localhost:8001/`, RabbitMQ Management — на `http://localhost:15672/`.

#### 3. Запуск в фоне

```bash
docker compose up -d
```

#### 4. Просмотр логов

```bash
docker compose logs -f web       # только Django
docker compose logs -f worker    # только Celery Worker
docker compose logs -f beat      # только Celery Beat
docker compose logs -f           # все сервисы сразу
```

#### 5. Остановка

```bash
docker compose stop              # остановить, не удаляя контейнеры
docker compose down              # остановить и удалить контейнеры
docker compose down -v           # остановить, удалить контейнеры и volume с БД
```

#### 6. Сброс данных и перезапуск

```bash
docker compose down -v
docker compose up
```

#### Состав сервисов

| Сервис     | Назначение                          | Порт        |
|------------|-------------------------------------|-------------|
| `postgres` | База данных PostgreSQL 12           | 5433        |
| `rabbitmq` | Брокер сообщений для Celery         | 5672, 15672 |
| `web`      | Django + gunicorn                   | 8001        |
| `worker`   | Celery Worker (обработка задач)     | —           |
| `beat`     | Celery Beat (планировщик по Cron)   | —           |

#### Сохранение данных (volumes)

**postgres_data** — named volume. При первом `docker compose up` Docker создаёт
директорию на хосте (`~/.docker/volumes/blog_postgres_data/`) и монтирует её
внутрь контейнера как `/var/lib/postgresql/data`. Все файлы БД пишутся туда.

Volume живёт независимо от контейнера:
- `docker compose down` — контейнер удаляется, volume остаётся
- `docker compose up` — создаётся новый контейнер, подхватывается тот же
  volume с теми же данными

Посмотреть список volumes:
```bash
docker volume ls
```

Удалить volume (стерёт БД целиком):
```bash
docker volume rm blog_postgres_data
# или
docker compose down -v
```

**.:/code/** — bind mount. Твоя папка проекта монтируется напрямую в `/code/`
контейнера. Любые изменения в файлах на macOS сразу видны внутри контейнера
(удобно для разработки — не нужно пересобирать образ при каждом изменении кода).

#### Подключение к PostgreSQL в контейнере

Проброшенный порт `5433:5432` — снаружи (macOS) порт 5433, внутри контейнера 5432.

**Снаружи** (через проброшенный порт контейнера):
```bash
psql -U blog_user -h 127.0.0.1 -p 5433 -d blog
```
Пароль: `123456`

**Снаружи** (через проброшенный порт контейнера):
```bash
psql -U blog_user -h 127.0.0.1 -p 5433 -d blog
```

**Войти в контейнер:**
```bash
docker exec -it postgres sh
psql -U blog_user -d blog
```

---

### Запуск локально (без Docker)

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
Пароль: `123456` (указан в `app/.env`)

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
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  rabbitmq:3-management
```

#### 5. Celery Worker

```bash
cd app && celery -A blog worker -l info
```

#### 6. Celery Beat

```bash
cd app && celery -A blog beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

#### 7. Flower (мониторинг Celery)

```bash
cd app && celery flower -A blog --address=127.0.0.1 --port=5555
```


### Начальные данные (data migration)

В проекте есть миграция `app/article/migrations/0004_seed_data.py`, 
которая наполняет БД стартовыми данными с помощью `RunPython`.

#### Что создаётся

- **Автор:** Алексей Кузнецов
- **Теги:** Python, Django, Web, Базы данных, DevOps
- **5 статей:**
  - Оптимизация SQL-запросов в Django ORM
  - CI/CD для Django: GitHub Actions + Docker
  - WebSockets в Django с Channels
  - PostgreSQL: полезные фишки для разработчика
  - Тестирование Django-приложений: от юнитов до интеграционных

#### Применение

На чистой БД миграция применяется автоматически при первом запуске:
```bash
python app/manage.py migrate
```

Если база уже была заполнена вручную (через shell) или нужно перезапустить:
```bash
python app/manage.py migrate article 0003
python app/manage.py migrate
```
Первая команда откатывает миграцию seed, вторая применяет заново.

#### Проверка

```bash
python app/manage.py shell -c "from article.models import Article; print(f'{Article.objects.count()} статей')"
```

#### Добавление своих данных

Чтобы добавить новые стартовые данные, создайте пустую миграцию:
```bash
python app/manage.py makemigrations article --empty
```
В полученном файле добавьте `migrations.RunPython(forward_func, reverse_func)`, где `forward_func` создаёт данные, а `reverse_func` (опционально) удаляет их.

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
* настроить nginx, gunicorn

