import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from event.views import EventViewSet


factory = APIRequestFactory()
view = EventViewSet.as_view({'get':'list'})

class Methods(TestCase):

    def test_post(self):
        request = factory.post('events/', {
            'name':'Lorem ipsum hackathon',
            'starts_at':'2020-01-02',
            'origin_url':'https://hackathonturkiye.com',
            'description':'Test test test test',
            'location':'online'
        })
        response = view(request)
        TestCase.assertEqual(response.status_code, 200)


    def test_get(self):
        request = factory.get('events/?location=online&format=json')
        response = view(request)
        response.render()
        content = json.loads(response.content)
        TestCase.assertEqual(content['results'][0]['location'], 'online')