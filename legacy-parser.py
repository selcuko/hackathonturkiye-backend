import json
import django
import requests
django.setup()
from django.contrib.auth.models import User
from event.models import Event, EventType
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files import File

jr = open("legacy.json")
j = json.load(jr)["hackathons"]

a = User.objects.get(email="omrfyyz@gmail.com")
t = EventType.objects.last()

for i, entry in enumerate(j):
    print("Processing entry index", i)

    try:
        e = Event(
            name = entry["name"],
            origin_url = entry["url"],
            description = entry["description"],
            starts_at = datetime.fromtimestamp(entry["date"]//1000),
            added_by = a,
        )

        try:
            e.ends_at = datetime.fromtimestamp(entry["dateEnd"]//1000)
        except Exception as ex:
            print("End date not specified. Passing...")
        
        try:
            r = requests.get(entry["imageUrl"])
            e.thumbnail.save("thumb.png", BytesIO(r.content))
        except Exception as ex:
            print(ex)
            print("Cannot save thumbnail. Passing...")
            e.save()
    
    except Exception as ex:
        print("Loop broke at", i)
        raise ex