from django.contrib import sitemaps
from django.urls import reverse

class HomeSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
        return ['homepage']

    def location(self, item):
        return reverse(item)
