from django.db import models
from auth.models import Author


class Post(models.Model):
    title = models.CharField(max_length=140)
    summary = models.TextField(max_length=2000)
    text = models.TextField(max_length=1024**2)
    published = models.BooleanField(default=False)
    
    authors = models.ManyToManyField(Author)

    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=None)


    
