from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from event import views as event_views
from profile import views as profile_views
from blog import views as blog_views
from rest_framework import routers
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='HackathonTurkiye API')

router = routers.DefaultRouter()
router.register(r'events', event_views.EventViewSet)
router.register(r'eventtypes', event_views.EventTypeViewSet)
router.register(r'groups', profile_views.GroupViewSet)
router.register(r'users', profile_views.UserViewSet)
router.register(r'posts', blog_views.PostViewSet)
router.register(r'postcategories', blog_views.PostCategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('schema/', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)
