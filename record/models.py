from django.db import models
from django.contrib.auth.models import User
from event.models import Event


class AbstractRecord(models.Model):
    """
    Abstract class for recording usage statistics.
    Not recommended to be used directly.
    """

    remote_addr = models.CharField(max_length=15)
    path = models.CharField(max_length=128)
    query_string = models.CharField(max_length=1024)
    user_agent = models.CharField(max_length=1024)
    method = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    debug = models.BooleanField(default=False)


class EventRecord(Abstract):
    """
    Used for event tracking
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

