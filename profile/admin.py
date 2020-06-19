from django.contrib import admin
from profile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    exclude = ['user']


admin.site.register(Profile, ProfileAdmin)
