from django.contrib import admin
from article.models import *

class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'sourse_link', 'code') # authors
    list_filter = ('title', 'pub_date', 'sourse_link')

admin.site.register(Article, AdminArticle)
admin.site.register(Tag)
admin.site.register(Site)
admin.site.register(Author)
