import os
import sys

import django
import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from news.models import Article


def save_article(title, link, website):
    try:
        Article.objects.get(link=link)
        print(f"Duplicate found: {title}")
    except Article.DoesNotExist:
        Article.objects.create(link=link, title=title, website=website)
        print(f"Article saved: {title}")


def scrap_website():
    url = "https://rugbyrama.fr"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.findAll("a", class_="article-link")

    for article in articles:
        title = article.get_text()
        link = article['href']
        save_article(title, link, 'rugbyrama')


if __name__ == "__main__":
    scrap_website()
