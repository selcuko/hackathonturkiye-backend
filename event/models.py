from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify


class EventType(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class EventTag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=140, null=True)
    body = models.TextField(max_length=10240, null=True, blank=True)
    etype = models.ForeignKey(EventType, on_delete=models.SET_NULL,
                              blank=True, null=True, 
                              verbose_name="Event type")
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=64,
    )

    origin_url = models.URLField()
    internal_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='thumbnails', 
        default='thumbnails/none/placeholder.jpg',
        max_length=1024)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    prize = models.CharField(max_length=20, blank=True, null=True)
    priority = models.IntegerField(default=1)
    holder = models.CharField(max_length=20, null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = models.ManyToManyField(EventTag, related_name='eventtag')

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('starts_at',)

    def __str__(self):
        return f"{self.name} ({self.starts_at.year})"
    
    def is_applicable(self):
        return datetime.now() > self.deadline if self.deadline else None
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=False)
        super().save(*args, **kwargs)

