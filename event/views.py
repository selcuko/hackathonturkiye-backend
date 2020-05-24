from django.views import View
from rest_framework import viewsets

from event.models import Event, EventType
from event.serializers import *


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventSerializer
    queryset = Event.objects.filter(published=True).order_by('-added_at')
    
    def get_queryset(self):
        params = self.request.query_params
        print("request params", params)

        etype = params.get('etype', None)
        if etype:
            print("filtering for event type", etype)
            etype = EventType.objects.get(name=etype)
            self.queryset = self.queryset.filter(etype=etype)
        
        after = params.get('after', None)
        if after:
            print("selecting events after", after)
            self.queryset = self.queryset.where('starts_at__grea', after)

        return self.queryset


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
