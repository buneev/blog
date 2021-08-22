from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    email = models.EmailField()

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
    resourse = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(blank=True)
    sourse_link = models.URLField(blank=True)
    code = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=150, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    authors = models.ManyToManyField("Author", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article_detail_url", kwargs={"id": self.id})

    class Meta:
        ordering = ['-pub_date']
