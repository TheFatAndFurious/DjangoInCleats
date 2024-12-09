from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='logos/')
    url = models.URLField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)  # Unique constraint
    published_at = models.DateTimeField(auto_now_add=True)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)
    admin_comment = models.TextField(null=True)
    is_featured = models.BooleanField(default=False)
    image = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.title
