from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about']  # Names of your URL patterns

    def location(self, item):
        return reverse(item)