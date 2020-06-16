from .models import Tag
from action_serializer import ModelActionSerializer
from rest_framework import serializers




class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']






