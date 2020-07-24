from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=80)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article_detail_url", kwargs={"id": self.id})


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title