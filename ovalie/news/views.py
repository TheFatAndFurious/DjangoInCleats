from django.shortcuts import render
from .models import Article, KeywordGroup
from django.core.paginator import Paginator

def article_list(request):
    # fetch articles from the DB
    team = request.GET.get('team')
    if team:
        print(f"value for {team}")
        articles = Article.objects.filter(keywords__name__iexact=team).distinct()
        print(f"{articles}")
    else:
        articles = Article.objects.prefetch_related('keywords').order_by('-published_at')

    # fetch featured articles
    # TODO: use the articles fetching method instead of fetching several times the same data
    featured_articles = Article.objects.prefetch_related('keywords').filter(is_featured=True).order_by('-published_at')[:3]

    # fetch TOP 14 teams
    teams = KeywordGroup.objects.filter(is_top14=True)


    #pagination
    paginator = Paginator(articles, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('HX-Request'):
        return render(request, 'partials/articles_list_by_tag.html', {
            'page_obj': page_obj,
            'teams': teams,
            'featured_articles': featured_articles})
    else:
        return render(request, 'news/articles_list.html', {
            'page_obj': page_obj,
            'teams': teams,
            'featured_articles': featured_articles})


