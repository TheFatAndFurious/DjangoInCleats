from django.shortcuts import render
from ovalie.news.models import Articles

def article_list(request):
    articles = Articles.objects.order_by('-published_at')
    return render(request, 'news/articles_list.html', {'articles': articles})

