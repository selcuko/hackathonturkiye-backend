from blog.serializers import *
from rest_framework import viewsets


class PostCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()
    
    def get_queryset(self):
        self.queryset = self.queryset
        return self.queryset


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status='p')

