import sys, os, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from ovalie.news.services.RugbyDevsService import get_matches_from_league
from ovalie.news.repositories.RugbyDevsRepository import GameRepository


def check_upcoming_games(round_id:int):

    games_data = get_matches_from_league(round_id)
    GameRepository.save_matches(games_data)
    print(f"we gucci my G")


