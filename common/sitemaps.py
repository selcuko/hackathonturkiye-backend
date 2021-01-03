from django.contrib.sitemaps import Sitemap
from .models import Tag


class TagSitemap(Sitemap):
    protocol = 'https'
    
    def items(self):
        return Tag.objects.all()
    
    def location(self, instance):
        try:
            return f'/etiket/{instance.slug}/tag'
        except:
            return 'bir şeyler çok fena ters gitti'
    
    def lastmod(self, instance):
        try:
            return instance.created_at
        except:
            return None
    