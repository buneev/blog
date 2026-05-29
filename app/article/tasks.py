from __future__ import absolute_import, unicode_literals

import logging
import socket

import kombu
from celery import shared_task
from django.db.models import Count
from django.utils import timezone
from django.conf import settings

from article.models import Article, Tag

logger = logging.getLogger(__name__)


@shared_task(name="article.tasks.count_articles")
def count_articles():
    """
    Считает количество статей и логирует общее число с датой последней.
    Период: каждые 2 минуты.
    """
    total = Article.objects.count()
    last = Article.objects.order_by('-created_at').first()
    last_date = last.created_at.strftime('%d.%m.%Y %H:%M') if last else '—'
    logger.info(f"[Article Stats] Всего статей: {total} | Последняя: {last_date}")


@shared_task(name="article.tasks.publish_article_stats")
def publish_article_stats():
    """
    Публикует статистику статей (количество, теги) в очередь RabbitMQ.
    Собирает общее количество статей и количество по каждому тегу,
    затем публикует JSON-сообщение в очередь article_stats.
    Период: каждые 2 минуты.
    """
    total = Article.objects.count()
    last = Article.objects.order_by('-created_at').first()
    tag_stats = {}

    for tag in Tag.objects.annotate(article_count=Count('article')):
        tag_stats[tag.title] = tag.article_count

    message = {
        'total_articles': total,
        'last_article_date': last.created_at.isoformat() if last else None,
        'last_article_title': last.title if last else None,
        'tags': tag_stats,
        'timestamp': timezone.now().isoformat(),
    }

    broker_url = settings.CELERY_BROKER_URL
    exchange = kombu.Exchange('article', type='direct', durable=True)
    queue = kombu.Queue('article_stats', exchange=exchange, routing_key='article_stats')

    with kombu.Connection(broker_url) as conn:
        producer = conn.Producer(serializer='json')
        queue(conn).declare()
        producer.publish(
            message,
            exchange=exchange,
            routing_key='article_stats',
            declare=[queue],
        )

    logger.info(f"[RabbitMQ] Опубликована статистика: {total} статей, {len(tag_stats)} тегов")


@shared_task(name="article.tasks.consume_article_stats")
def consume_article_stats():
    """
    Читает одно сообщение из очереди article_stats и логирует его.
    Если сообщений нет, логирует отсутствие новых данных.
    Период: каждую минуту.
    """
    broker_url = settings.CELERY_BROKER_URL
    exchange = kombu.Exchange('article', type='direct', durable=True)
    queue = kombu.Queue('article_stats', exchange=exchange, routing_key='article_stats')

    def _handle(body, message):
        logger.info(f"[RabbitMQ Consumer] Получено сообщение: {body}")
        message.ack()

    with kombu.Connection(broker_url) as conn:
        queue(conn).declare()
        with conn.Consumer(queue, callbacks=[_handle], accept=['json']):
            try:
                conn.drain_events(timeout=1)
            except socket.timeout:
                logger.info("[RabbitMQ Consumer] Новых сообщений нет")



