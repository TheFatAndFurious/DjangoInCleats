from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.order_by('-published_at')
    featured_articles = Article.objects.filter(is_featured=True).order_by('-published_at')[:3]
    return render(request, 'news/articles_list.html', {
        'articles': articles,
        'featured_articles': featured_articles})


