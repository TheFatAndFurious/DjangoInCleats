import requests, sys, os, django, datetime
from dateutil.parser import parse
from django.db import transaction
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()


headers = {
	"x-rapidapi-key": "2a3f462634msh63a4a8280da611ep1352acjsn54d03d9ef887",
	"x-rapidapi-host": "rugby-devs.p.rapidapi.com"
}

def get_matches_from_league(round_id: int):
	url = "https://rugby-devs.p.rapidapi.com/matches"
	querystring = {"round_id":f"eq.{round_id}","lang":"en","offset":"0"}
	response = requests.get(url, headers=headers, params=querystring)
	return response.json()


