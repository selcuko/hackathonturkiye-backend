from blog.models import *
from profile.serializers import *
from rest_framework import serializers


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer(many=False, read_only=False)
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = [
            'title',
            'summary',
            'body',
            'published_at',
            'author',
            'category',
        ]
    
    def create(self, validated_data):
        request = self.context["request"]
        user = request.user

        validated_data.update({
            'author': user,
            'read': len(validated_data['body'])//500,
        })

        return Event.objects.create(added_by=user, **validated_data)


