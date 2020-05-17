from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework import viewsets
from event.models import Event
from event.serializers import *


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-added_at')

class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
