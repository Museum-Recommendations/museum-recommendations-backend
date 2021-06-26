from django.db import models

# Create your models here.

class MuseumObject(models.Model):
	title = models.CharField(max_length=255)
	inventory_num = models.CharField(max_length=50)
	photo = models.ImageField(upload_to="object_images/", blank=True)
	model3d = models.FileField(upload_to="object_3dmodels/", blank=True)
	# could add more information about object


