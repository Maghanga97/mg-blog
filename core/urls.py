from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', views.robot_texts),
    path('', views.index ),
    path('details/<slug:slug>/', views.post_details),
    path('category/<slug:slug>/', views.get_category_posts),
    path('search/', views.search)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)