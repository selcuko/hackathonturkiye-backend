from django.contrib import admin
from django.utils.html import mark_safe
from blog.models import Post, PostCategory, PostTag
from csvexport.actions import csvexport


class PostAdmin(admin.ModelAdmin):
    actions = [csvexport]
    change_actions = ['preview']
    fields = (
        'preview',
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
        'preview',
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

    def preview(self, instance):
        return mark_safe(f'<a href="https://hackathonturkiye.com/blog/{instance.slug}/?preview=yes">Sitede gör</a>')


admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
