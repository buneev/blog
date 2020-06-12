from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/article/{self.id}/"
        return reverse("article:article-detail", kwargs={"id": self.id})