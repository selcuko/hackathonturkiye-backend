from django.contrib import admin
from blog.models import Post, PostCategory, PostTag
from csvexport.actions import csvexport


class PostAdmin(admin.ModelAdmin):
    actions = [csvexport]
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
        'priority',
        'published_at',
        'time',
    )
    readonly_fields = [
        'created_at',
        'edited_at',
        #'published_at',
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
