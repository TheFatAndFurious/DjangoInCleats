from django.core.management.base import BaseCommand
import sys, os, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()
from news.services.tasks import RugbyDevsTasks
class Command(BaseCommand):
    help = "Fetch rugby data"

    def handle(self, *args, **options):
        RugbyDevsTasks.check_upcoming_games()
