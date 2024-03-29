import instauto.api.actions.structs.post as ps
from instauto.api.client import ApiClient
import json
from event.models import Event
from PIL import Image
from random import randint
import io, os

caption_template = """
📍 %(ename)s

%(esum)s

📍Konum: %(eloc)s

📍Son Başvuru: %(edeadline)s

📍Detaylar ve başvuru: %(elink)s



%(etags)s
"""


client = None


def init():
    global client
    auth_file = json.load(open("instagram_auth.json"))
    username, password = auth_file['username'], auth_file['password']
    try:
        print('Trying to load Instagram session from file.')
        client = ApiClient.initiate_from_file('/tmp/.instauto')
    except:
        print('Logging in to Instagram...', end='\t')
        client = ApiClient(username=username, password=password)
        client.log_in()
        print('OK')
    client.save_to_disk('/tmp/.instauto')






def post_event(event: Event):
    try:
        if client is None: init()

        hashtags = ''
        for tag in event.tags.all():
            hashtags += f'#{tag.slug.replace("-", "")} '

        caption = caption_template % {
            'ename':event.name,
            'eloc':event.location,
            'esum':event.description,
            'edeadline':event.deadline.strftime('%d %B %Y'),
            'elink':event.url,
            'etags':hashtags
        }
        photo_path = convert_photo(event.thumbnail.path)
        post = ps.PostFeed(photo_path, caption)
        response = client.post_post(post)
        return True, response

    except Exception as exc:
        print(f'{exc!r}', exc.args)
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


def convert_photo(path):
    photo = Image.open(path)
    if not photo.mode == 'RGB': photo = photo.convert('RGB')
    final_path = f'/tmp/hturkiye{randint(100, 999)}.jpg'
    photo.save(final_path, 'JPEG')
    return final_path
