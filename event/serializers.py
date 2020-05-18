from rest_framework import serializers
from event.models import Event, EventType


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context["request"]
        user = request.user

        if validated_data.get('added_by', None):
             validated_data.pop('added_by')

        return Event.objects.create(added_by=user, **validated_data)
        
    

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'
