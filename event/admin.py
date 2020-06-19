from django.contrib import admin
from event.models import *


class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'starts_at',
        'published',
        'holder',
    ]
    list_filter = ['etype', 'published']
    exclude = ['added_by']
    


admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
#admin.site.register(EventTag)
