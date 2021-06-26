from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from recommendations.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt

from get_objects.models import MuseumObject
from django.contrib.auth.models import User

from .models import UserReview

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
    
    exhibit = MuseumObject.objects.get(pk=request.POST["object_id"])
    user = User.objects.get(username=source_review["username"])
    review = UserReview(user = user,
            reviewed_object = exhibit,
            joi = source_review["joi"],
            empathy = source_review["empathy"],
            thoughtfulness = source_review["thoughtfulness"]
            )

    review.save()
    ###########################################################
    # use ml to find out the next exhibit id 
    ###########################################################
    dummy_id = 1


    # next_exhibit = MuseumObject.objects.get(pk=dummy_id)
    # image_data = base64.b64encode(next_exhibit.image).decode('utf-8')
    # image_data = str(next_exhibit.image)
    # response = {"next object id" : next_exhibit.id , 
        # "next object name" : next_exhibit.name,
        # "next object image url" : image_data,
        # "description": next_exhibit.description}
    # return HttpResponse(json.dumps(response))
    return HttpResponse(json.dumps({"some data": "some data"}))
