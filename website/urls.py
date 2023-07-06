from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import Sitemap


sitemaps = {"posts": Sitemap}
urlpatterns = [
    path("", views.home, name="home"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
