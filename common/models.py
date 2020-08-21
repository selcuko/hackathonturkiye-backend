from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(editable=False, unique=True)
    description = models.TextField(null=True, editable=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.lower().replace('ı', 'i'), allow_unicode=False)
        super().save(*args, **kwargs)
    
    def in_events(self):
        return self.events.all()
    
    def in_posts(self):
        return self.posts.all()
