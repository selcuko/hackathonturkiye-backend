from django.contrib import admin
from event.models import *
from django.contrib import messages
from csvexport.actions import csvexport
from django_object_actions import DjangoObjectActions


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
        print('TWEET', obj)
        messages.success(request, 'Tweetlendi.')
    



admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
#admin.site.register(EventTag)
