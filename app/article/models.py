from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField('опубликовано', auto_now_add=True)
    updated_at = models.DateTimeField('обновлено', auto_now=True)
    pub_date = models.DateTimeField('опубликовано в первоисточнике', blank=True, null=True)
    sourse_link = models.URLField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=400, blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True, null=True)
    authors = models.ManyToManyField("Author", blank=True, null=True)
    rating = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article_detail_url", kwargs={"id": self.id})

    class Meta:
        ordering = ['-pub_date']

class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
class Site(models.Model):
    name = models.CharField(max_length=200)
    resourse = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']