from django.shortcuts import render
from .models import Article, KeywordGroup, Videos, Game
from django.core.paginator import Paginator
from .services.ArticleService import ArticleService
from django.http import HttpResponse, JsonResponse
from .utils import get_vite_asset_path
from django.conf import settings


# Creating dynamic links for js and css files
vite_js = get_vite_asset_path('src/main.ts', file_type="file")
vite_css = get_vite_asset_path('src/main.ts', file_type="css")
vite_css_link = vite_css[0]


def comments(request, article_id):
    canonical_url = request.build_absolute_uri()
    article = Article.objects.filter(id=article_id)
    print(article)
    return render(request, 'news/comments.html', {
        'vite_css': vite_css_link,
        'vite_js': vite_js,
        'unique_identifier': article_id,
        'canonical_url': canonical_url,
        'article': article[0]
    })

def articles_page(request):
    featured_articles = Article.objects.prefetch_related('keywords').filter(is_featured=True).order_by('-published_at')[:20]

    return render(request, 'news/featured_articles.html', {
        'vite_css': vite_css_link,
        'vite_js': vite_js,
        'featured_articles': featured_articles
    })

def about(request):
    return render(request, 'news/about.html',{
        'vite_css': vite_css_link,
        'vite_js': vite_js,
    })

def robots_txt(request):
    content = """
    User-agent: *
    Disallow: /admin/

    Sitemap: https://paparugby.com/sitemap.xml
    """
    return HttpResponse(content, content_type="text/plain")

def home(request):
    # fetch articles from the DB
    team = request.GET.get('team', 'all_teams')
    language = request.GET.get('language', 'french')
    videos = request.GET.get('videos', 'top14')
    articles = ArticleService.filter_articles(team,language)

    # upcoming games for the banner
    upcoming_games = Game.objects.filter(round_number=15)
    league_name = None
    round_number = None
    if upcoming_games:
        league_name = upcoming_games[0].league
        round_number = upcoming_games[0].round_number

    # TODO: use the articles fetching method instead of fetching several times the same data
    featured_articles = Article.objects.prefetch_related('keywords').filter(is_featured=True).order_by('-published_at')[:20]

    selected_videos = Videos.objects.filter(is_visible=True).filter(categories__category__iexact=videos).order_by('-published_at')[:5]
    uprugby_video = Videos.objects.filter(channel="Up Rugby").order_by('-published_at')[:1]
    # fetch teams
    print(uprugby_video)
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
            # data for the banner
            'upcoming_games': upcoming_games,
            'league_name': league_name,
            'round_number': round_number,
            'vite_css': vite_css_link,
            'vite_js': vite_js,
            'uprugby_video': uprugby_video[0],
            'featured_articles': featured_articles})



