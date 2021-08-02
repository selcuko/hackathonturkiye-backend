from blog.serializers import *
from rest_framework import viewsets
from .models import PostTag, Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import PostSerializer

class PostPreview(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, slug, format=None):
        sketch = Post.objects.get(slug=slug)
        serial = PostSerializer(sketch)
        return Response(serial.data)

class PostCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status='p')
    lookup_field = 'slug'

    def get_queryset(self):
        params = self.request.query_params
        filters = {}
        non_fields = [
            'highlighted',
            'tag',
            'limit',
            'offset',
            'order_by',
            'tags'
        ]
        for p in params.keys():
            if p not in non_fields:
                filters[p] = params[p]

        tags = params.get('tags', None)
        if tags:
            tags = tags.split(',')
            for tag in tags:
                self.queryset = self.queryset.filter(tags__slug=tag).distinct()
        
        highlighted = params.get('highlighted', None)
        
        
        order_by = params.get('order_by', None)
        if order_by:
            self.queryset = self.queryset.order_by(order_by)
        elif not highlighted:
            self.queryset = self.queryset.order_by('-published_at')
        elif highlighted:
            self.queryset = self.queryset.order_by('-priority')
        
        category = params.get('category', None)
        if category:
            self.queryset = self.queryset.filter(category__name=category)
        
        self.queryset = self.queryset.filter(**filters)
                
        if highlighted:
            return self.queryset[:int(highlighted)]
        return self.queryset

    def retrieve(self, request, slug):
        if request.query_params.get('preview'):
            return Response(PostSerializer(Post.objects.get(slug=slug)).data)
        return super().retrieve(request, slug)



