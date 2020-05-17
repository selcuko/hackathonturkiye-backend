from django.db import models
from auth.models import Author

class Hackathon(models.Model):

    name = models.CharField(max_length=64)
    origin_url = models.URLField(default=None)
    internal_url = models.URLField(default=None)
    thumbnail = models.ImageField(upload_to='thumbnails')
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    duration = models.DurationField(default=None)
    published = models.BooleanField(default=True)

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
