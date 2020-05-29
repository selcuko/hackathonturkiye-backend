from django.test import TestCase
import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .views import *


class BlogTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testserver', password='testserver')
    
    def test_post(self):
        response = self.client.post(
            '/posts/', {
                'title': 'test',
                'summary': 'test',
                'body': 'püsküllü test',
            })
        self.assertEqual(response.status_code, 403, 'POST method publicly available')
        
    def test_get(self):
        response = self.client.get('/posts/?tag=mmm')
        self.assertEqual(response.status_code, 200, "Server couldn't return results")
