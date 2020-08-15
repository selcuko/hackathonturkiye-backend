from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'contact',
        'category__name',
        'email',
    ]
    list_filter = ['category__name']
    readonly_fields = '__all__'
    exclude = ['title', 'user_agent', 'remote_addr', 'path']



admin.site.register(ContactForm, ContactAdmin)
admin.site.register(ContactFormCategory)
