import json
from io import BytesIO
import requests
from datetime import date, datetime
import django
django.setup()
from django.core.files import File
from event.models import Event, EventType

FILE = './boiga-cyanea-export.json'
events = json.load(open(FILE))["hackathons"]



def get_type(name, url='https://localhost'):
    name = name.lower()
    if EventType.objects.exists(name=name):
        return EventType.objects.get(name=name)
    e = EventType(
        name=name,
    )
    e.save()
    return e

types = [
    "hackathon",
    "educathon",
    "ideathon",
    "designathon",
    "datathon",
    "game",
]


for i, e in enumerate(events):
    print(f'Processing entry no #{i}')
    date = e['date'] // 1000
    date = datetime.fromtimestamp(date)
    date = str(date)
    ev = Event.objects.get(name=e['name'], starts_at=date)

    try:
        b = BytesIO(requests.get(e["imageUrl"]).content)
        ev.thumbnail.save('thumbnail.png', File(b))
    except:
        print(f"Cannot get thumbnail for entry no #{i}")
        ev.thumbnail = None
        ev.save()
