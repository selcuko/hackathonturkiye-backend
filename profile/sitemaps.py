from django.contrib.sitemaps import Sitemap
from .models import Profile


class ProfileSitemap(Sitemap):
    protocol = 'https'
    
    def items(self):
        return [profile.user for profile in Profile.objects.all()]
    
    def location(self, instance):
        try:
            return f'/blog?author__username={instance.username}'
        except:
            return 'bir şeyler çok fena ters gitti'
    
    def lastmod(self, instance):
        try:
            return instance.date_joined
        except:
            return None