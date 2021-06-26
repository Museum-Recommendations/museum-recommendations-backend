from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from recommendations.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt

import os 
import base64
from PIL import Image
import json

# Create your views here.
@csrf_exempt
def get_next_object(request):
    # image_path = os.path.join(BASE_DIR, 'get_objects', 'image.jpg')
    # img = Image.open(image_path)
    
    # with open(image_path, "rb") as image_file:
    #     image_data = base64.b64encode(image_file.read()).decode('utf-8')
    print("score that we recieved: {}".format(request.POST))
    response = {"next object" : "lithuanian clay vase", 
        "description": "This vase was found in the backpack of the Belarusian extremist Protasevich, as proof of the participation of the West in the Belarusian elections"}
    return HttpResponse(json.dumps(response))
    # return HttpResponse(json.dumps({"some data": "some data"}))
