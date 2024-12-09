from django.contrib import admin
from .models import Articles

@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'published_at')
