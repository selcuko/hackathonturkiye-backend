from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'contact',
        'category',
        'email',
        'created_at',
    ]
    list_filter = ['category']



admin.site.register(ContactForm, ContactAdmin)
admin.site.register(ContactFormCategory)
