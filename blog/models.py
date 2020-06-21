from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from common.models import Tag

class PostCategory(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Post category"
        verbose_name_plural = "Post categories"


class PostTag(models.Model):
    name = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    status_codes = (
        ("d", "Draft"),
        ("c", "Review"),
        ("p", "Publish")
    )
    title = models.CharField(max_length=1400)
    summary = models.TextField(max_length=2000, blank=True, null=True)
    body = RichTextField(max_length=1024**2)
    status = models.CharField(max_length=1, choices=status_codes, default="d")
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=1400,
        unique=True,
    )
    thumbnail = models.ImageField(upload_to='blog/thumbnails', default='blog/none.png', max_length=1024)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey(PostCategory, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    # statistical
    priority = models.IntegerField(default=1)
    read = models.IntegerField(default=1)
    time = models.IntegerField(default=1)

    # autofilled
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def published(self) -> bool:
        return self.status == 'p'

    def author_name(self): pass

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.lower().replace('ı', 'i'), allow_unicode=False)
        self.time = len(self.body.split(" ")) // 200
        if not self.published_at and self.published(): self.published_at = self.created_at
        super().save(*args, **kwargs)
