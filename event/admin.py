from django.contrib import admin
from event.models import *
from csvexport.actions import csvexport


class EventAdmin(admin.ModelAdmin):
    actions = [csvexport]
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



admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
#admin.site.register(EventTag)
