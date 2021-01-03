from django.contrib.sitemaps import Sitemap
from .models import Event


class EventSitemap(Sitemap):
    protocol = 'https'
    
    def items(self):
        return Event.objects.filter(published=True)
    
    def location(self, instance):
        try:
            return f'/etkinlik/{instance.slug}'
        except:
            return 'bir şeyler çok fena ters gitti'
    
    def lastmod(self, instance):
        try:
            return instance.added_at
        except:
            return None



class LocationSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return list(set([e.location for e in Event.objects.filter(location__isnull=False)]))
    
    def location(self, item):
        return f'/etkinlikler/hepsi/{item}'


class EventTypeSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return list(set([e.etype for e in Event.objects.filter(etype__isnull=False)]))
    
    def location(self, item):
        return f'/etkinlikler/{item}'