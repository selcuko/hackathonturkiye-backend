from django.db import models
from django.contrib.auth.models import User


class EventType(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name.capitalize()


class Event(models.Model):

    name = models.CharField(max_length=64)
    description = models.TextField(max_length=140, default='')
    body = models.TextField(max_length=10240, default='')
    etype = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)
    origin_url = models.URLField(default=None)
    internal_url = models.URLField(default=None)
    thumbnail = models.ImageField(upload_to='thumbnails')
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    published = models.BooleanField(default=True)

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-starts_at',)
    
    def __str__(self):
        return f"{'[YAYINLANMADI] ' if not self.published else ''}\
            {self.name}"
