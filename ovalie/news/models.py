from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)  # Unique constraint
    published_at = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.title