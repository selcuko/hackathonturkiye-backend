from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Tag
from .cross import CrossSearchTagSerializer
from .serializers import TagSerializer


class CrossSearchTagViewSet(ModelViewSet):
    lookup_field = 'slug__iexact'
    serializer_class = CrossSearchTagSerializer
    queryset = Tag.objects.all()


class TagViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

