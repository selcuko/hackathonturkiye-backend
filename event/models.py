from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from djrichtextfield.models import RichTextField
from django.utils.text import slugify
from django.core.exceptions import MultipleObjectsReturned
from common.models import Tag


class EventType(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class EventTag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=640)
    description = models.TextField(max_length=1400, null=True)
    body = RichTextField(blank=True, null=True)
    etype = models.ForeignKey(EventType, on_delete=models.SET_NULL,
                              blank=True, null=True, 
                              verbose_name="Event type")
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=64,
        unique=True
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
    location = models.CharField(max_length=1000, blank=True, null=True)
    prize = models.CharField(max_length=200, blank=True, null=True)
    priority = models.IntegerField(default=1)
    holder = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name='events')

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('starts_at',)

    def __str__(self):
        return f"{self.name} ({self.starts_at.year})"
    
    def is_applicable(self):
        return timezone.now() > self.deadline if self.deadline else None
    
    def has_details(self):
        return bool(self.body)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.lower().replace('ı', 'i'), allow_unicode=False)
        try:
            self.validate_unique()
        except:
            self.slug += f'pk-{self.pk}'
            self.validate_unique()
        super().save(*args, **kwargs)

