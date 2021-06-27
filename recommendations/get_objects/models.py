from django.db import models
from django.utils.html import mark_safe
from django.shortcuts import reverse

# Create your models here.

class MuseumObject(models.Model):
    title = models.CharField(max_length=255)
    inventory_num = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/object_images/", blank=True)
    model3d = models.FileField(upload_to="static/object_3dmodels/", blank=True)
    # could add more information about object

    def __str__(self):
        return self.inventory_num

    @property
    def image_tag(self):
        print("=====================used")
        return mark_safe(f'<img src="{self.image}" />')