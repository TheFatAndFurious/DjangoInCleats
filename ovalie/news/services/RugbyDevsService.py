import requests

url = "https://rugby-devs.p.rapidapi.com/standings"

querystring = {"league_id":"eq.3098","season_id":"eq.47860","lang":"en","offset":"0"}

headers = {
	"x-rapidapi-key": "2a3f462634msh63a4a8280da611ep1352acjsn54d03d9ef887",
	"x-rapidapi-host": "rugby-devs.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())