from django.contrib import admin
from blog.models import Post, PostCategory, PostTag


class PostAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'summary',
        ('category', 'tags'),
        'body',
        'status',
        'created_at',
        'author',
        'edited_at',
        'thumbnail',
    )
    readonly_fields = [
        'created_at',
        'edited_at',
    ]
    list_display = [
        'title',
        'summary',
        'author',
        'published'
    ]
    list_filter = [
        'status',
        'author',
    ]


admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
