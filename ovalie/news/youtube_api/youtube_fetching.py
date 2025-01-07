import requests


CHANNEL_ID = "UCpH-VFo4_F2oMYiW8942mQw"
API_KEY = "AIzaSyAaBWQgnLvxuGR4gdDBPOzBMfgmLTLl0V4"

def get_uploads(api_key, channel_id, max_results=5):
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet&type=video&order=date&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()
    print(data)

get_uploads(API_KEY, CHANNEL_ID)

