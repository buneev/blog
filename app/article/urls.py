from django.urls import path
from .views import *

app_name = 'article'
urlpatterns = [
    path('', article_list, name='article-list'),
    path('create/', article_create, name='article-create'),
    path('<int:id>/', article_detail, name='article-detail'),
    path('<int:id>/update/', article_update, name='article-update'),
    path('<int:id>/delete/', article_delete, name='article-delete'),
]