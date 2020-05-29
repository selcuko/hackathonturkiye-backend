from django.test import TestCase
from django.contrib.auth.models import User
from .models import *



class ContactFormTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='testserver', password='testserver')
        ContactFormCategory.objects.create(name='test', url=None)

    def test_is_publicly_readable_better_not(self):
        self.client.logout()
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 403, 'Contact forms are publicly readable.')
    
    def test_is_auth_user_can_read(self):
        logged = self.client.login(username='testserver', password='testserver')
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200, 'Contact forms GET method not working.')
        self.client.logout()

    def test_post(self):
        self.client.logout()
        response = self.client.post('/contact/', {
            'title': 'ggg',
            'category.name': 'test',
            'email': 'j@gh.com',
            'body': "test",
            'contact': 'johny'
        })

        self.assertEqual(response.status_code, 201, 'POST method not working (not logged in)')
        
