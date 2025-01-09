import os
import sys

import django
from django.db.models import Q
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()
from news.models import Article

class ArticleService:
    @staticmethod
    def filter_articles(team: str, language: str):
        filters = Q()


        return Article.objects.filter(filters).prefetch_related('keywords').order_by('-published_at')