from django.contrib.auth.models import User
from rest_framework import serializers
from event.models import Event, EventType


class EventSerializer(serializers.HyperlinkedModelSerializer):
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
            'origin_url',
        )
        
    
    def create(self, validated_data):

        request = self.context["request"]
        user = request.user if isinstance(request.user, User) else None

        if validated_data.get('added_by', None):
             validated_data.pop('added_by')

        return Event.objects.create(added_by=user, **validated_data)
        
    

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'
