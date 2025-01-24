import os
import sys

import django
from django.db.models import Q
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()
from ovalie.news.models import Article

class ArticleService:
    @staticmethod
    def filter_articles(team: str, language: str):
        filters = Q()

        if language == 'french':
            filters &= Q(is_french_language=True)
        elif language == 'english':
            filters &= Q(is_french_language=False)

        if team == 'top14':
            filters &= Q(keywords__league='top14')
        elif team == 'prod2':
            filters &= Q(keywords__league='prod2')
        elif team != 'all_teams':
            filters &= Q(keywords__name__iexact=team)

        return Article.objects.filter(filters).filter(is_visible=True).prefetch_related('keywords').order_by('-published_at')