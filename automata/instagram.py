from typing import final
import instagram_private_api
import json
from event.models import Event
from PIL import Image
from random import randint
import io

caption_template = """
📍 %(ename)s

%(esum)s

📍Konum: %(eloc)s

📍Son Başvuru: %(edeadline)s

📍Detaylar ve başvuru: %(elink)s
"""


api = None


def init():
    global api
    auth_file = json.load(open("instagram_auth.json"))
    username, password = auth_file['username'], auth_file['password']
    api = instagram_private_api.Client(username, password)





def post_event(event: Event):
    try:
        if api is None: init()
        photo_output, photo_size = prepare_photo(event.thumbnail.path)
        photo_binary = photo_output.getvalue()
        caption = caption_template.format(
            ename=event.name,
            eloc=event.location,
            esum=event.description,
            edeadline=event.deadline,
            elink=event.url
        )
        api.post_photo(photo_binary, photo_size, caption)
        return True, None
    except Exception as exc:
        return False, exc



def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def prepare_photo(photo_path):
    photo = Image.open(photo_path)
    photo = crop_max_square(photo)
    if not photo.mode == 'RGB': photo = photo.convert('RGB')
    # final_path = f'/temp/hturkiye{randint(100, 999)}.jpeg'
    output = io.BytesIO()
    photo.save(output, 'JPEG')
    size = photo.size
    return output, size