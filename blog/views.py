from blog.serializers import *
from rest_framework import viewsets
from .models import PostTag

class PostCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()
    
    def get_queryset(self):
        params = self.queryset.query_params

        tags = params.get('tag', None)
        if tag:
            self.queryset = self.queryset.filter(tags__name=tag)
                
        return self.queryset


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status='p')

