from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
