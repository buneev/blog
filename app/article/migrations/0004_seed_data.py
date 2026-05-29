from django.db import migrations, transaction
from django.utils import timezone


def seed_data(apps, schema_editor):
    Article = apps.get_model('article', 'Article')
    Author = apps.get_model('article', 'Author')
    Tag = apps.get_model('article', 'Tag')

    with transaction.atomic():
        author, _ = Author.objects.get_or_create(
            name="Алексей",
            surname="Кузнецов",
        )

        tags = {}
        for name in ["Python", "Django", "Web", "Базы данных", "DevOps"]:
            tag, _ = Tag.objects.get_or_create(title=name)
            tags[name] = tag

        articles_data = [
            {
                "title": "Оптимизация SQL-запросов в Django ORM",
                "text": "Грамотная работа с ORM — залог производительности Django-приложения. Рассматриваем select_related, prefetch_related, annotate, агрегатные функции и кеширование QuerySet на реальных примерах.",
                "tags": ["Django", "Python", "Базы данных"],
            },
            {
                "title": "CI/CD для Django: GitHub Actions + Docker",
                "text": "Настройка непрерывной интеграции и доставки для Django-проекта. Автоматические тесты, сборка Docker-образа, деплой на VPS. Пример рабочего пайплайна с нуля.",
                "tags": ["DevOps", "Web", "Python"],
            },
            {
                "title": "WebSockets в Django с Channels",
                "text": "Реализация реального времени в Django: Channels, ASGI, consumers, WebSocket-аутентификация. Создаём чат и уведомления для веб-приложения.",
                "tags": ["Django", "Python", "Web"],
            },
            {
                "title": "PostgreSQL: полезные фишки для разработчика",
                "text": "Оконные функции, CTE, индексы, полнотекстовый поиск — возможности PostgreSQL, которые должен знать каждый backend-разработчик. Примеры запросов и сравнение производительности.",
                "tags": ["Базы данных", "DevOps"],
            },
            {
                "title": "Тестирование Django-приложений: от юнитов до интеграционных",
                "text": "Полный гайд по тестированию: pytest-django, Factory Boy, mock, coverage. Как писать быстрые и надёжные тесты, которые реально ловят баги.",
                "tags": ["Django", "Python", "DevOps"],
            },
        ]

        for data in articles_data:
            tag_titles = data.pop("tags")
            article, created = Article.objects.get_or_create(
                title=data["title"],
                defaults={
                    **data,
                    "pub_date": timezone.now(),
                    "rating": 0,
                },
            )
            if created:
                article.tags.set(tags[t] for t in tag_titles)
                article.authors.add(author)


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210905_1657'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=migrations.RunPython.noop),
    ]
