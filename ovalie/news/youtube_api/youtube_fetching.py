from unicodedata import category

import django
import requests
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from news.models import Videos

RUGBYPASSFR_CHANNEL_ID = "UC8yDQBIfghpQCrJufJCGmIA"
URC_CHANNEL_ID = "UC-S6cXyil4qbIPfb2hrcH4w"
TOP14_CHANNEL_ID = "UCWrD2VhZdO-_W8QDBxiXmeg"
PROD2_CHANNEL_ID = "UCu98ro1AIOu-4wtZxDRS6Tg"
UP_RUGBY_CHANNEL_ID = "UCpH-VFo4_F2oMYiW8942mQw"

links = [RUGBYPASSFR_CHANNEL_ID, UP_RUGBY_CHANNEL_ID, TOP14_CHANNEL_ID, PROD2_CHANNEL_ID, UP_RUGBY_CHANNEL_ID]

API_KEY = "AIzaSyAaBWQgnLvxuGR4gdDBPOzBMfgmLTLl0V4"


def save_videos(videos):
    existing_links = set(Videos.objects.values_list('link', flat=True))

    videos_objects = [
        Videos(
            title = video.get('title'),
            description = video.get('description'),
            link = video['link'],
            channel = video.get('channel'),
        )
        for video in videos if video['link'] not in existing_links
    ]

    if videos_objects:
        Videos.objects.bulk_create(videos_objects)

    print(f"{len(videos_objects)} new videos added to the database")


def get_uploads(api_key, channel_id, max_results=5):
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet&type=video&order=date&videoEmbeddable=true&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()
    videos = []

    # Here we will construct an array containing the last 5 videos from the channel
    # If for whatever reason no link is provided for an item then we will skip that item
    category = ''
    match channel_id:
        case "UCWrD2VhZdO-_W8QDBxiXmeg":
            category = 'top14'
        case "UCu98ro1AIOu-4wtZxDRS6Tg":
            category ='prod2'
        case "UCpH-VFo4_F2oMYiW8942mQw":
            category = 'uprugby'
        case "UC8yDQBIfghpQCrJufJCGmIA":
            category = 'rugbypass'

    for item in data.get('items', []):

        video_id = item.get('id', {}).get('videoId')
        if not video_id:
            continue
        if item.get('status', {}).get('embeddable', False):
            continue
        description = item.get('snippet', {}).get('description', None)
        title = item.get('snippet', {}).get('title', None)
        channel = item.get('snippet', {}).get('channelTitle', None)

        # Building the video link before saving it
        link = f"http://www.youtube.com/embed/{video_id}"

        videos.append({
            'title': title,
            'description': description,
            'link': link,
            'channel': channel,
            'categories': category
        })
    save_videos(videos)

for link in links:

    get_uploads(API_KEY, link)

