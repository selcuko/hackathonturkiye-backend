from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from auth.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
