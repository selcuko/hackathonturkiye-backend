from blog.models import *
from rest_framework import serializers


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = PostCategorySerializer(
        many=True,
        read_only=False,
    )
    class Meta:
        model = Post
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context["request"]
        user = request.user

        if validated_data.get('author', None):
             validated_data.pop('author')

        return Event.objects.create(added_by=user, **validated_data)


