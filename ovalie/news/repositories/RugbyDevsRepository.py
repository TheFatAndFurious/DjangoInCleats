import sys, os, django
from dateutil.parser import parse
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from ovalie.news.models import Game

class GameRepository:
    @staticmethod
    def save_matches(matches_data):
        upcoming_games = []

        for game in matches_data:
            try:
                upcoming_games.append({
                    "game_id": game.get('id', 0),
                    "league": game.get('tournament_name', 'unknown'),
                    "round_id": game.get('round_id', 0),
                    "round_number": game.get('round', {}).get('round', None),
                    "home_team_name": game.get('home_team_name', 'Unknown'),
                    "home_team_id": game.get('home_team_id', 0),
                    "away_team_name": game.get('away_team_name', 'Unknown'),
                    "away_team_id": game.get('away_team_id', 0),
                    "start_time": game.get('times', {}).get('specific_start_time', None),
                    "status": game.get('status_type', 'Unknown'),
                    "score_home": game.get('home_team_score', {}).get('current', 0),
                    "score_away": game.get('away_team_score', {}).get('current', 0),
                })
            except Exception as e:
                print(f"Error processing game: {e}")

        for game in upcoming_games:
            Game.objects.update_or_create(
                game_id=game['game_id'],
                defaults={
                    'league':game['league'],
                    'round_id':game['round_id'],
                    'round_number':game['round_number'],
                    'home_team_name':game['home_team_name'],
                    'home_team_id':game['home_team_id'],
                    'away_team_name':game['away_team_name'],
                    'away_team_id':game['away_team_id'],
                    'start_time':parse(game['start_time']) if game['start_time'] else None,
                    'status':game['status'],
                    'score_home':game['score_home'],
                    'score_away':game['score_away']
                }
            )
