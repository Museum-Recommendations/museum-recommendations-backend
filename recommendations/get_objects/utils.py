import os
from recommendations.settings import BASE_DIR
from .models import MuseumObject

IMAGES_DIR = 'object_images'

def get_photo_url(inventory_num):
    museum_object = MuseumObject.objects.get(inventory_num=inventory_num)
    if museum_object.image:
        image_path = str(museum_object.image)
    image_path = os.path.join(BASE_DIR, image_path)
    return image_path
