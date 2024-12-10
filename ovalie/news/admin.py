from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'published_at', 'website', 'is_visible', 'is_featured', 'image')
    list_filter = ('is_visible', 'is_featured', 'website', 'image')
    search_fields = ('title', 'website')
