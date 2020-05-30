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
            'offset',
            'order_by'
        ]
        for p in params.keys():
            if p not in non_fields:
                filters[p] = params[p]

        tag = params.get('tag', None)
        if tag:
            self.queryset = self.queryset.filter(tags__name=tag).distinct()
        
        order_by = params.get('order_by', None)
        if order_by:
            self.queryset = self.queryset.order_by('priority', order_by)
        else:
            self.queryset = self.queryset.order_by('priority')
        
        if len(filters):
            self.queryset = self.queryset.filter(**filters)
            if 'pk' in filters.keys() and len(self.queryset) > 0:
                p = self.queryset[0]
                p.read =+ 1
                p.save()
                
        return self.queryset




