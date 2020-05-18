from django.db import models
from django.contrib.auth.models import User


class EventType(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=140, default='')
    body = models.TextField(max_length=10240, default='')
    etype = models.ForeignKey(EventType, on_delete=models.SET_NULL,
                              blank=True, null=True, 
                              verbose_name="Event type")

    origin_url = models.URLField()
    internal_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='thumbnails', default='thumbnails/none/placeholder.jpg')
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_online = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('-starts_at',)

    def __str__(self):
        return f"{self.name}, {self.starts_at.year}"
