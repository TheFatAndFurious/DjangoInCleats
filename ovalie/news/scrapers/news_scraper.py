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


def scrap_rugbyrama():
    url = "https://rugbyrama.fr"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.findAll("a", class_="article-link")

    for article in articles:
        title = article.get_text()
        link = article['href']
        save_article(title, link, 'rugbyrama')

def scrap_rugbynistere():
    url = 'https://lerugbynistere.fr'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("a", class_="title")

    for article in articles:
        title = article.get_text()
        link = article['href']
        save_article(title, link, "rugbynistere")

def scrap_acturugby():
    global title
    url = 'https://dicodusport.fr/blog/actualites/rugby/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("li", class_="mvp-blog-story-wrap")

    for article in articles:
        is_title = article.find("h2")
        if is_title:
            title = is_title.text
        link = article.find("a")
        linktosave = link['href']
        save_article(title, linktosave, "dicodusport")


if __name__ == "__main__":
    scrap_rugbyrama()
    scrap_rugbynistere()
    scrap_acturugby()
