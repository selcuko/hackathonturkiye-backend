from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory, APIClient


#factory = APIRequestFactory()
#request = factory.get('/')

client = APIClient()
client.get('/')