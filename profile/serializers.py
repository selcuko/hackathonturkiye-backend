from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from profile.models import Profile


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(
        many=False,
        read_only=True,
    )
    class Meta:
        model = User
        fields = [
            "email", 
            "username", 
            "first_name", 
            "last_name", 
            "profile",
            "groups",
            ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
