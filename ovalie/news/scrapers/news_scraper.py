import os
import sys

import django
import requests
from bs4 import BeautifulSoup



sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovalie.settings')
django.setup()

from ovalie.news.models import Article, Website, KeywordGroup


def run_all_scrapers():
    print("Scraper therugbyrama")
    scrap_rugbyrama()

    print("Scraping dicodusport")
    scrap_acturugby()

    print("Scraping rugbynistere")
    scrap_rugbynistere()

    print("Scraping lequipe")
    scrap_lequipe()

    print("Scraping rugbypass")
    scrap_rugbypass()

    print("Scraping ladepeche")
    scrap_ladepeche_pro()

    print("Scraping sudouest")
    #scrap_sudouest()
    print("all scrapers ran successfully, we gucci")

def save_article(title, link, website_name, is_french_language=True, is_visible=True):
    website, _ = Website.objects.get_or_create(name=website_name)

    article, created = Article.objects.get_or_create(
        link=link,
        defaults={'title': title, 'website': website, 'is_french_language':is_french_language, 'is_visible':is_visible}
    )

    if created:
        # Assign multiple keyword groups
        groups = check_if_keywords(title)
        article.keywords.set(groups)

        # Assign a default image from the first matching group
        if not article.image and groups:
            article.image = groups[0].image
        article.save()

        print(f"Article saved: {title} ")
    else:
        print(f"Duplicate article: {title}")

def check_if_keywords(title):
    matched_groups = []
    for group in KeywordGroup.objects.all():
        for keyword in group.keywords:
            if keyword.lower() in title.lower():
                matched_groups.append(group)
    return matched_groups

def scrap_rugbyrama():
    url = "https://rugbyrama.fr"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.findAll("a", class_="article-link")

    for article in articles:
        title = article.get_text()
        link = url + article['href']
        save_article(title, link, 'rugbyrama')

def scrap_ladepeche_pro():
    url = "https://www.ladepeche.fr/sport/rugby-xv/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("a", class_="stretched-link")

    for article in articles:
        title = article.get_text()
        link = url + article["href"]
        save_article(title, link, "ladepeche", is_visible=False)

def scrap_sudouest():
    url = "https://www.sudouest.fr/sport/rugby/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("div", class_="article-wrapper")

    for article in articles:
        is_title = article.find("h2")
        if not is_title:
            continue
        title = is_title.text

        link = article.find("a")
        if not link or link.get("href"):
            continue

        linktosave = url + link['href']
        save_article(title, linktosave, "Sud-Ouest", is_visible=False)

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


def scrap_rugbypass():
    url = "https://www.rugbypass.com/global/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("a", class_="link-box")

    for article in articles:
        # print(f"Processing article: {article}")

        title = article.get("aria-label")
        link = article.get("href")

        if title and link:
            save_article(title, link, "rugbypass", False)
        else:
            print(f"Skipping article due to missing 'aria-label' or 'href': {article}")


def scrap_lequipe():
    url = "https://www.lequipe.fr/Rugby/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("a", class_="ChronoItem__link")

    for article in articles:
        title = article.get_text()
        link = "https://www.lequipe.fr" + article["href"]
        save_article(title, link, "lequipe")

# if __name__ == "__main__":
#     run_all_scrapers()
