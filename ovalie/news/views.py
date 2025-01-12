from django.shortcuts import render
from .models import Article, KeywordGroup, Videos
from django.core.paginator import Paginator
from .services.ArticleService import ArticleService

def about(request):
    return render(request, 'news/about.html')

def home(request):
    # fetch articles from the DB
    team = request.GET.get('team', 'all_teams')
    print(f"coucou")
    print(team)
    language = request.GET.get('language', 'french')
    videos = request.GET.get('videos', 'top14')
    articles = ArticleService.filter_articles(team,language)
    print(articles)
    # Here we are using params to filter articles by team
    # if the 'team' value being received is equals to 'all_teams' then we will fetch all articles regardless of teams


    # fetch featured articles
    # TODO: use the articles fetching method instead of fetching several times the same data
    featured_articles = Article.objects.prefetch_related('keywords').filter(is_featured=True).order_by('-published_at')[:10]

    selected_videos = Videos.objects.filter(is_visible=True).filter(categories__category__iexact=videos).order_by('-published_at')[:5]

    # fetch teams
    top14_teams = KeywordGroup.objects.filter(league='top14')
    prod2_teams = KeywordGroup.objects.filter(league='prod2')


    #pagination
    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('Hx-Target') == 'articles-container':
        return render(request, 'partials/block_news_list.html', {
            'page_obj': page_obj,
            'top14_teams': top14_teams,
            'prod2_teams': prod2_teams
        })
    elif request.headers.get('Hx-Target') == 'videos-container':
        return render(request, 'partials/block_videos.html', {
            'videos': selected_videos
        })
    else:
            return render(request, 'news/home.html', {
            'page_obj': page_obj,
            'top14_teams': top14_teams,
            'prod2_teams': prod2_teams,
            'videos': selected_videos,
            'featured_articles': featured_articles})


