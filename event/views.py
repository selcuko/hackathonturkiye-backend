from datetime import date
from django.views import View
from django.core.exceptions import FieldError
from rest_framework import viewsets
from rest_framework.response import Response

from event.models import Event, EventType
from event.serializers import *


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = Event.objects.filter(published=True).order_by('starts_at')
    serializer_class = EventSerializer
    
    def retrieve(self, **kwargs):
        queryset = Event.objects.all()
        serializer = ExtentedEventSerializer(queryset, many=False)
        return Response(serializer.data)

    
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
            "order_by",
            'tags'
        ]
        params = self.request.query_params

        # depreceated, use combination of order_by and limit instead
        highlighted = params.get('highlighted', None)
        if highlighted is not None:
            return self.query.order_by('priority', 'starts_at')[:int(highlihted)]
        
        # single event (details) request
        pk = params.get('pk', None)
        if pk is not None:
            pass


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
        
        tags = params.get('tags', None)
        if tags:
            tags = tags.lower().split(',')
            for tag in tags:
                self.queryset = self.queryset.filter(tags__name=tag).distinct()
        
        # filter: by date
        after = params.get('after', None)
        before = params.get('before', None)
        if after:
            self.queryset = self.queryset.filter(starts_at__gt=after)
        else:
            self.queryset = self.queryset.filter(starts_at__gt=str(date.today()))
        if before:
            self.queryset = self.queryset.filter(starts_at__lt=before)
        
        if len(filters):
            self.queryset = self.queryset.filter(**filters)
        return self.queryset

    def retrieve(self, request, pk):
        obj = Event.objects.get(pk=pk)
        ser = EventSerializer(obj)
        return Response(ser.data)


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
