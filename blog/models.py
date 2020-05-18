from django.db import models
from django.contrib.auth.models import User


class PostCategory(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=140)
    summary = models.TextField(max_length=2000, blank=True, null=True)
    text = models.TextField(max_length=1024**2)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
