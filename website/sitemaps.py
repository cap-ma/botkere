from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from . import models


class MySitemap(Sitemap):
    def items(self):
        return ["main", "about", "license"]

    def location(self, item):
        return reverse(item)
