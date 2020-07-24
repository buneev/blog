from django.urls import path
from .views import *


app_name = 'article'
urlpatterns = [
    path('', article_list, name='article_list_url'),
    path('<int:id>/', article_detail, name='article_detail_url'),
    path('tag/<str:name>', tag_detail, name='tag_detail_url'),
    path('create/', article_create, name='article_create_url'),
    path('<int:id>/update/', article_update, name='article_update_url'),
]