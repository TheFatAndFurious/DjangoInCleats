from django.core.management.base import BaseCommand
import sys, os, django


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from news.scrapers.news_scraper import (run_all_scrapers)

class Command(BaseCommand):
    help = "Fetch articles"

    def handle(self, *args, **options):
        run_all_scrapers()
