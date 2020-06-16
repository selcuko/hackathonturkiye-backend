from .models import Tag
from action_serializer import ModelActionSerializer
from rest_framework import serializers
from event.serializers import EventSerializer
from blog.serializers import PostSerializer

class CrossSearchTagSerializer(serializers.ModelSerializer):
    in_posts = PostSerializer(many=True, read_only=True)
    in_events = EventSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = ['name', 'in_events', 'in_posts']