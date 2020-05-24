from django.views import View
from rest_framework import viewsets

from event.models import Event, EventType
from event.serializers import *


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventSerializer
    queryset = Event.objects.filter(published=True)
    
    def get_queryset(self):
        params = self.request.query_params
        print("request params", params)

        # filter: by event type
        etype = params.get('etype', None)
        if etype:
            try:
                etype = EventType.objects.get(name=etype)
                self.queryset = self.queryset.filter(etype=etype)
            except EventType.DoesNotExist:
                # todo: make below line more elegant
                self.queryset = self.queryset[:0]
        
        # filter: by location
        location = params.get('location', None)
        if location:
            self.queryset = self.queryset.filter(location=location)
        
        # order: by parameter
        order_by = params.get('order_by', None)
        if order_by:
            try:
                self.queryset = self.queryset.order_by(order_by)
            except self.FieldError:
                # todo: make below line more elegant
                self.queryset = self.queryset[:0]
        else:
            self.queryset = self.queryset.order_by('-added_at')

        return self.queryset


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
