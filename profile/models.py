from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=200, blank=True)

    linkedin = models.URLField()
    instagram = models.URLField()


"""
Tying up Profile objects with User objects
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created: return
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()