from django.contrib import admin
from .models import Article, Website, KeywordGroup, Videos


class KeywordGroupInline(admin.TabularInline):
    model = Article.keywords.through  # Access the through table for the Many-to-Many relationship
    extra = 1  # Number of empty rows to show for adding new entries


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [KeywordGroupInline]  # Add inline for editing keywords
    list_display = ('title', 'link', 'published_at', 'website', 'is_visible', 'is_featured', 'is_french_language', 'is_video', 'image')
    list_filter = ('is_visible', 'is_featured', 'website')
    search_fields = ('title', 'website')

@admin.register(Videos)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'description', 'is_visible')


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'logo')


@admin.register(KeywordGroup)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'keywords', 'is_top14', 'image', 'color')
