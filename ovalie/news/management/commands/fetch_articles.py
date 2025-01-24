from django.core.management.base import BaseCommand
import sys, os, django


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
django.setup()

from ovalie.news.scrapers.news_scraper import (run_all_scrapers)

class Command(BaseCommand):
    help = "Fetch articles"

    def handle(self, *args, **options):
        run_all_scrapers()
