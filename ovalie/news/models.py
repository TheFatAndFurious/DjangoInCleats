from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='static/news/images/logos/')
    url = models.URLField()

    def __str__(self):
        return self.name

class KeywordGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    keywords = models.JSONField(blank=True, null=True)
    image = models.ImageField(upload_to='static/news/images/keywords_images', null=True, blank=True)
    color = models.CharField(max_length=7, default="#000000")

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
    image = models.ImageField(upload_to='static/news/article_image')
    keywords = models.ManyToManyField(KeywordGroup, blank=True)
    def __str__(self):
        return self.title
