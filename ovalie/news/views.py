from django.shortcuts import render
from .models import Article, KeywordGroup, Videos
from django.core.paginator import Paginator

def about(request):
    return render(request, 'news/about.html')

def home(request):
    # fetch articles from the DB
    team = request.GET.get('team', 'all_teams')
    language = request.GET.get('language', 'french')
    articles = []

    # Here we are using params to filter articles by team
    # if the 'team' value being received is equals to 'all_teams' then we will fetch all articles regardless of teams
    if team == 'all_teams':
        match language:
            case "french":
                articles = Article.objects.filter(is_french_language=True).prefetch_related('keywords').order_by('-published_at')
            case "english":
                articles = Article.objects.filter(is_french_language=False).prefetch_related('keywords').order_by('-published_at')
            case "all_articles":
                articles = Article.objects.prefetch_related('keywords').order_by('-published_at')
    else:
        match language:
            case "french":
                articles = Article.objects.filter(keywords__name__iexact=team).filter(is_french_language=True).distinct().order_by('-published_at')
            case "english":
                articles = Article.objects.filter(keywords__name__iexact=team).filter(is_french_language=False).distinct().order_by('-published_at')
            case "all_articles":
                articles = Article.objects.filter(keywords__name__iexact=team).distinct().order_by('-published_at')

    # fetch featured articles
    # TODO: use the articles fetching method instead of fetching several times the same data
    featured_articles = Article.objects.prefetch_related('keywords').filter(is_featured=True).order_by('-published_at')[:10]

    videos = Videos.objects.filter(is_visible=True).order_by('-published_at')

    # fetch TOP 14 teams
    teams = KeywordGroup.objects.filter(is_top14=True)


    #pagination
    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('HX-Request'):
        return render(request, 'partials/block_news_list.html', {
            'page_obj': page_obj,
            'teams': teams,
            'videos': videos,
            'featured_articles': featured_articles})
    else:
        return render(request, 'news/home.html', {
            'page_obj': page_obj,
            'teams': teams,
            'videos': videos,
            'featured_articles': featured_articles})


