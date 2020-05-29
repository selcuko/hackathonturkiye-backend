from django.contrib.auth.models import User
from rest_framework import serializers
from event.models import Event, EventType


class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = ['name', 'url']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    etype = EventTypeSerializer(
        many=False,
        read_only=False
    )
    class Meta:
        model = Event
        fields = (
            'pk',
            'name',
            'description',
            'starts_at',
            'ends_at',
            'priority',
            'holder',
            'prize',
            'location',
            'etype',
            'origin_url',
        )
        
    
    def create(self, validated_data):

        request = self.context["request"]
        user = request.user if isinstance(request.user, User) else None
        event_type = validated_data['etype']['name']
        etype = EventType.objects.get(name=event_type)
        validated_data.update({
            'added_by': user,
            'etype': etype
        })

        return Event.objects.create(**validated_data)
        
    

