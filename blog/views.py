from blog.serializers import *
from rest_framework import viewsets
from .models import PostTag, Post


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
        
        order_by = params.get('order_by', None)
        if order_by:
            self.queryset = self.queryset.order_by('priority', order_by)
        else:
            self.queryset = self.queryset.order_by('priority')
        
        self.queryset = self.queryset.filter(**filters)
                
        return self.queryset




