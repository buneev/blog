from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    author = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article-detail", kwargs={"id": self.id})


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title