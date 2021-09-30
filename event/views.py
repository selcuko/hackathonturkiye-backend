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
    queryset = Event.objects.filter(published=True)
    serializer_class = EventSerializer
    lookup_field = 'slug'

    def get_queryset(self):
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

        # set priority of past events to 1
        self.queryset.filter(priority__gt=1, deadline__lt=today).update(priority=1)

        status = params.get('status', None)
        if status:
            if status == 'ongoing':
                self.queryset = self.queryset.filter(deadline__lte=today, ends_at__gte=today)
            elif status == 'finished':
                self.queryset = self.queryset.filter(ends_at__lte=today)
            elif status == 'future':
                self.queryset = self.queryset.filter(deadline__gte=today)

        filters = {}
        for key, value in params.items():
            if key not in nonfield:
                filters[key] = value

        # filter: by event type
        etype = params.get('etype', None)
        if etype:
            self.queryset = self.queryset.filter(etype__name=etype)
            

        tags = params.get('tags', None)
        if tags:
            tags = tags.lower().split(',')
            for tag in tags:
                self.queryset = self.queryset.filter(tags__slug=tag).distinct()

        # filter: by date
        after = params.get('after', None)
        before = params.get('before', None)
        if after:
            self.queryset = self.queryset.filter(deadline__gt=after)

        if before:
            self.queryset = self.queryset.filter(deadline__lt=before)


        order_by = params.get('order_by', None)
        if order_by:
            self.queryset = self.queryset.order_by('-priority', order_by)
        else:
            self.queryset = self.queryset.order_by('-priority', 'deadline')
        
        return self.queryset


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
