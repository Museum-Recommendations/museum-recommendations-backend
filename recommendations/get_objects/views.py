from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from recommendations.settings import BASE_DIR

import os 
import base64
from PIL import Image
import json

# Create your views here.
def get_object_info(request):
    image_path = os.path.join(BASE_DIR, 'get_objects', 'image.jpg')
    img = Image.open(image_path)
    
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    return HttpResponse(json.dumps({"some data": "some data"}))