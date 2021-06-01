from django.contrib import admin
from event.models import *
from django.contrib import messages
from csvexport.actions import csvexport
from django_object_actions import DjangoObjectActions
from .tweeter import tweet_event

class EventAdmin(DjangoObjectActions, admin.ModelAdmin):
    actions = [csvexport]
    change_actions = ['tweet_this']
    list_display = [
        'name',
        'starts_at',
        'published',
        'holder',
        'etype',
        'deadline',
    ]
    list_filter = ['etype', 'published', 'priority',]
    exclude = ['added_by', 'internal_url']

    def tweet_this(self, request, obj):
        success, extra = tweet_event(obj)
        if success == True:
            messages.success(request, f'Tweet gönderildi. {extra.source_url}')
        else:
            messages.error(request, f'Tweet gönderilirken hata oluştu: {extra!r}')
    tweet_this.label = 'Bunu Tweetle'




admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
#admin.site.register(EventTag)
