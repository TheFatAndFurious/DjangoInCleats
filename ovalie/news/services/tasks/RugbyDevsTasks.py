import sys, os, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from news.services.RugbyDevsService import get_matches_from_league
from news.repositories.RugbyDevsRepository import GameRepository


def check_upcoming_games():

    games_data = get_matches_from_league(422152)
    print(games_data)
    GameRepository.save_matches(games_data, 'Pro D2')
    print(f"we gucci my G")


