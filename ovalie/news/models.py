from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='static/news/images/logos/')
    url = models.URLField()
    banner = models.ImageField(upload_to='static/news/images/banners/', null=True)

    def __str__(self):
        return self.name

class KeywordGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    keywords = models.JSONField(blank=True, null=True)
    image = models.ImageField(upload_to='static/news/images/keywords_images', null=True, blank=True)
    color = models.CharField(max_length=7, default="#000000")
    is_top14 = models.BooleanField(default=False)
    league = models.CharField(max_length=50, null=True)

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
    image = models.ImageField(upload_to='images')
    keywords = models.ManyToManyField(KeywordGroup, blank=True)
    is_french_language = models.BooleanField(default=True)
    is_video = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class VideoCategory(models.Model):
    category = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='static/news/images/video_categories', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

class Videos(models.Model):
    title = models.CharField(max_length=255, blank=True)
    link = models.URLField(unique=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(VideoCategory, blank=True)
    channel = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title

class Game(models.Model):
    game_id = models.IntegerField(unique=True)
    round_id = models.IntegerField()
    league = models.CharField(max_length=50, blank=True)
    round_number = models.IntegerField(blank=True)
    home_team_name = models.CharField(max_length=100)
    home_team_id = models.IntegerField()
    away_team_name = models.CharField(max_length=100)
    away_team_id = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=50)
    score_home = models.IntegerField(blank=True, null=True)
    score_away = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.league



