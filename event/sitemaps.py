from django.contrib.sitemaps import Sitemap
from .models import Event


class EventSitemap(Sitemap):
    changefreq = 'never'
    priority = .5
    
    def items(self):
        return Event.objects.filter(published=True)
    