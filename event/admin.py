from django.contrib import admin
from event.models import *


class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'starts_at',
        'published',
        'holder',
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
