from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class LessonListSitemap(Sitemap):
    def items(self):
        return []

    def location(self, obj):
        return reverse('home')