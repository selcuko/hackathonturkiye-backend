from datetime import date
from django.views import View
from django.utils import timezone
from django.core.exceptions import FieldError
from rest_framework import viewsets
from rest_framework.response import Response

from event.models import Event, EventType
from event.serializers import *


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = Event.objects.all() #.filter(published=True)
    serializer_class = EventSerializer
    lookup_field = 'slug'


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
            'tags',
            'status',
        ]
        params = self.request.query_params
        today = str(timezone.now())
        #today = str(date.today())
        # depreceated, use combination of order_by and limit instead
        highlighted = params.get('highlighted', None)
        if highlighted is not None:
            return self.queryset.order_by('priority', 'starts_at')[:int(highlighted)]
        
        # single event (details) request
        pk = params.get('pk', None)
        if pk is not None:
            pass

        status = params.get('status', None)
        if status:
            if status == 'ongoing':
                self.queryset = self.queryset.filter(starts_at__lte=today, ends_at__gte=today)
            elif status == 'finished':
                self.queryset = self.queryset.filter(ends_at__lte=today)
            elif status == 'future':
                self.queryset = self.queryset.filter(starts_at__gte=today)
        


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
            # ie try this somewhen
            # self.queryset.filter(etype__name=etype)
        
        tags = params.get('tags', None)
        if tags:
            tags = tags.lower().split(',')
            for tag in tags:
                self.queryset = self.queryset.filter(tags__slug=tag).distinct()
        
        # filter: by date
        after = params.get('after', None)
        before = params.get('before', None)
        if after:
            self.queryset = self.queryset.filter(starts_at__gt=after)
        else:
            if not (status):
                self.queryset = self.queryset.filter(starts_at__gt=today)
        if before:
            self.queryset = self.queryset.filter(starts_at__lt=before)
        
        if len(filters):
            for f, q in filters.items():
                if f == 'location': self.queryset = self.queryset.filter(location__iexact=q)
                else: self.queryset = self.queryset.filter(**{f'{f}__iexact':q})
            #self.queryset = self.queryset.filter(**filters)
        
        order_by = params.get('order_by', None)
        if order_by:
            self.queryset = self.queryset.order_by(order_by)
        return self.queryset



class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
