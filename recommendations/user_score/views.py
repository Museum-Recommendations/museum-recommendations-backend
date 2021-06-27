from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from recommendations.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt

from get_objects.models import MuseumObject
from django.contrib.auth.models import User

from .models import UserReview
from get_objects.utils import get_photo_url

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
    
    source_review = request.POST
    
    exhibit = MuseumObject.objects.get(inventory_num=request.POST["object_num"])
    # user = User.objects.get(username=source_review["username"])
    review = UserReview(
            reviewed_object = exhibit,
            joi = source_review["joi"],
            empathy = source_review["empathy"],
            thoughtfulness = source_review["thoughtfulness"]
            )

    review.save()
    ###########################################################
    # use ml to find out the next exhibit id 
    ###########################################################
    dummy_num = "MK_228"


    museum_object = MuseumObject.objects.get(inventory_num=dummy_num)
    object_description = dict()
    object_description["inventory_num"] = museum_object.inventory_num
    object_description["title"] = museum_object.title

    if museum_object.image:
        object_description["image_url"] = get_photo_url(museum_object.inventory_num)
    else:
        object_description["image_url"] = ''

    if museum_object.model3d:
        object_description["model3d"] = "----------------------------------" # Not available right now

    return HttpResponse(json.dumps(object_description))
    # next_exhibit = MuseumObject.objects.get(pk=dummy_id)
    # image_data = base64.b64encode(next_exhibit.image).decode('utf-8')
    # image_data = str(next_exhibit.image)
    # response = {"next object id" : next_exhibit.id , 
        # "next object name" : next_exhibit.name,
        # "next object image url" : image_data,
        # "description": next_exhibit.description}
    # return HttpResponse(json.dumps(response))
    # return HttpResponse(json.dumps({"some data": "some data"}))
