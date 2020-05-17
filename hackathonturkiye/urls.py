from django.contrib import admin
from django.urls import path, include
from event import views as event_views
from profile import views as profile_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', event_views.EventViewSet)
router.register(r'eventtypes', event_views.EventTypeViewSet)
router.register(r'groups', profile_views.GroupViewSet)
router.register(r'users', profile_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
