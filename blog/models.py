from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class PostCategory(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Post category"
        verbose_name_plural = "Post categories"


class PostTag(models.Model):
    name = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    status_codes = (
        ("d", "Draft"),
        ("c", "Review"),
        ("p", "Publish")
    )
    title = models.CharField(max_length=140)
    summary = models.TextField(max_length=2000, blank=True, null=True)
    body = models.TextField(max_length=1024**2)
    status = models.CharField(max_length=1, choices=status_codes, default="d")
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=140,
    )

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey(PostCategory, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(PostTag, blank=True)

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
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=False)
        self.time = len(self.body.split(" ")) // 100
        super().save(*args, **kwargs)
