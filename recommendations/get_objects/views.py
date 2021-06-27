from django.shortcuts import render, reverse
from django.http import HttpResponse
from rest_framework.response import Response

from recommendations.settings import BASE_DIR
from .utils import get_photo_url
from .models import MuseumObject

import os 
import base64
from PIL import Image
import json

IMAGES_DIR = 'object_images'

def get_object_info(request, inventory_num=None):
    
    if inventory_num:
        museum_object = MuseumObject.objects.get(inventory_num=inventory_num)
        object_description = dict()
        object_description["inventory_num"] = museum_object.inventory_num
        object_description["title"] = museum_object.title

        if museum_object.image:
            object_description["image_url"] = request.build_absolute_uri(reverse("image", args=[inventory_num]))
        else:
            object_description["image_url"] = ''

        if museum_object.model3d:
            object_description["model3d"] = "----------------------------------" # Not available right now

        return HttpResponse(json.dumps(object_description))

    return HttpResponse("Test")



def get_object_photo(request, inventory_num):
    image_path = get_photo_url(inventory_num)
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return HttpResponse(image_data)