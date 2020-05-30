from blog.serializers import *
from rest_framework import viewsets
from .models import PostTag, Post


class PostCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status='p')
    
    def get_queryset(self):
        params = self.request.query_params
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

        tag = params.get('tag', None)
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
            if 'pk' in filters.keys() and len(self.queryset) > 0:
                p = self.queryset[0]
                p.read =+ 1
                p.save()
                
        return self.queryset




