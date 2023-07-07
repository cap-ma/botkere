from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from . import models


class MySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return models.Order.objects.all()
        # return ["telegram bot", "telegramda bot yasash", "bot"]

    def location(self, item):
        return reverse(item)

    def lastmod(self, obj):
        return obj.updated
