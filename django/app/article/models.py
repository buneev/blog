from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(blank=True)
    author = models.CharField(max_length=100, blank=True, default='')
    sourse_link = models.URLField(blank=True)
    code = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=150, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article_detail_url", kwargs={"id": self.id})


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
