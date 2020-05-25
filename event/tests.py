import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from event.views import EventViewSet



class Methods(TestCase):

    def setUp(self):
        User.objects.create_user(username='testserver', password='testserver')
        self.logged = self.client.login(username='testserver', password='testserver')


    def test_post(self):
        response = self.client.post('/events/', {
            'name':'Lorem ipsum hackathon',
            'starts_at':'2020-01-02T00:00',
            'origin_url':'https://hackathonturkiye.com',
            'description':'Test test test test',
            'location':'online'
        })
        print(response.content)
        self.assertEqual(response.status_code, 201, "Unwanted status code returned.")


    def test_get(self):
        location = 'online'
        response = self.client.get(f'/events/?location={location}&format=json')
        json = response.json()
        self.assertIsInstance(json.get('results', False), list, "Response was not containing a JSON.")
        results = json.get('results')
        for o in results:
            self.assertEqual(o.get(location, None), location, "Query string didn't do its job.")
        self.assertEqual(response.status_code, 200, 'Response code is not OK')