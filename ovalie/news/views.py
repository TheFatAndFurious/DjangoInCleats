from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator

def article_list(request):
    # fetch articles from the DB
    articles = Article.objects.order_by('-published_at')

    # fetch featured articles
    featured_articles = Article.objects.filter(is_featured=True).order_by('-published_at')[:3]

    #pagination
    paginator = Paginator(articles, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'news/articles_list.html', {
        'page_obj': page_obj,
        'featured_articles': featured_articles})


