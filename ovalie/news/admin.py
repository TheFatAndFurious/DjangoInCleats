from django.contrib import admin
from .models import Article
from .models import Website


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'published_at', 'website', 'is_visible', 'is_featured', 'image')
    list_filter = ('is_visible', 'is_featured', 'website', 'image')
    search_fields = ('title', 'website')

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'logo')

