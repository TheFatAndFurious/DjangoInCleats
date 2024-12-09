from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.order_by('-published_at')
    return render(request, 'news/articles_list.html', {'articles': articles})
