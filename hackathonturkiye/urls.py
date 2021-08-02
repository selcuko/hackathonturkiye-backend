from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog
from event import views as event_views
from event.sitemaps import EventSitemap, LocationSitemap, EventTypeSitemap
from profile import views as profile_views
from profile.sitemaps import ProfileSitemap
from blog import views as blog_views
from blog.sitemaps import PostSitemap
from contact import views as contact_views
from common import views as common_views
from common.sitemaps import TagSitemap
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.sitemaps.views import sitemap

admin.site.site_header = 'Hackathon Türkiye Yönetim Paneli'
admin.site.index_title = 'Yönetim Paneli'
admin.site.site_title = 'Hackathon Türkiye'

schema_view = get_schema_view(
   openapi.Info(
      title="HackathonTurkiye Backend API",
      default_version='v1',
      description="",
      terms_of_service="",
      contact=openapi.Contact(email="omrfyyz@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'events', event_views.EventViewSet, basename='event')
router.register(r'groups', profile_views.GroupViewSet)
router.register(r'users', profile_views.UserViewSet)
router.register(r'posts', blog_views.PostViewSet)
router.register(r'contact', contact_views.ContactFormViewSet)
router.register(r'tagsearch', common_views.CrossSearchTagViewSet, basename='tagsearch')
router.register(r'tags', common_views.TagViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('sitemap.xml', sitemap, {'sitemaps': {
      'events': EventSitemap,
      'blogs': PostSitemap,
      'authors': ProfileSitemap,
      'tags': TagSitemap,
      'etypes': EventTypeSitemap,
      'locations': LocationSitemap,
      }}),
   path('', include(router.urls)),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('blog_preview/<slug:slug>/', blog_views.PostPreview.as_view()),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('djrichtextfield/', include('djrichtextfield.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)
