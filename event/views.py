from datetime import date
from django.views import View
from django.core.exceptions import FieldError
from rest_framework import viewsets

from event.models import Event, EventType
from event.serializers import *


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventSerializer
    queryset = Event.objects.filter(published=True).order_by('starts_at')
    
    def get_queryset(self):
        

        # todo: find another method, im sure it exists
        nonfield = [
            "etype", 
            "offset", 
            "limit", 
            "page", 
            "format", 
            "highlighted",
            "after",
            "before",
            "order_by"
        ]
        today = str(date.today())
        params = self.request.query_params
        highlight = params.get('highlight', None)
        if highlight:
            return self.query.order_by('starts_at')[:5]
        filters = {}
        for key, value in params.items():
            if key not in nonfield:
                filters[key] = value

        # filter: by event type
        etype = params.get('etype', None)
        if etype:
            try:
                etype = EventType.objects.get(name=etype)
                self.queryset = self.queryset.filter(etype=etype)
            except EventType.DoesNotExist:
                # todo: make below line more elegant
                self.queryset = self.queryset.none()
        
        # order: by parameter
        order_by = params.get('order_by', None)
        if order_by:
            try:
                self.queryset = self.queryset.order_by(order_by)
            except FieldError:
                self.queryset = self.queryset.none()
        
        # filter: by date
        after = params.get('after', None)
        before = params.get('before', None)
        if after:
            self.queryset = self.queryset.filter(starts_at__gt=after)
        else:
            self.queryset = self.queryset.filter(starts_at__gt=today)
        if before:
            self.queryset = self.queryset.filter(starts_at__lt=before)
        
        if len(filters):
            self.queryset = self.queryset.filter(**filters)
        return self.queryset


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
