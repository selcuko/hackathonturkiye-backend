from django.contrib import admin
from django.urls import path, include
from event import views as event_views
from auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', event_views.EventViewSet)
router.register(r'eventtypes', event_views.EventTypeViewSet)
router.register(r'groups', auth_views.GroupViewSet)
router.register(r'users', auth_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
