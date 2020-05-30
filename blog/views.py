from blog.serializers import *
from rest_framework import viewsets
from .models import PostTag

class PostCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()
    
    def get_queryset(self):
        params = self.queryset.query_params
        filters = {}
        non_fields = [
            'highlighted',
            'tag',
            'limit',
            'offset'
        ]
        for p in params.keys():
            if p not in non_fields:
                filters[p] = params[p]

        tags = params.get('tag', None)
        if tag:
            self.queryset = set(self.queryset.filter(tags__name=tag))
        
        highlighted = params.get('highlighted', None)
        if highlighted:
            try:
                value = int(highlighted)
            except ValueError:
                value = 5
            self.queryset = self.queryset.order_by('priority', 'created_at')[:value]
        
        if len(filters):
            self.queryset = self.queryset.filter(**filters)
                
        return self.queryset


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status='p')

