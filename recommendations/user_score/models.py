from django.db import models
from get_objects.models import MuseumObject
# Create your models here.

class UserReview(models.Model):
    reviewed_object = models.ForeignKey(MuseumObject, on_delete=models.CASCADE)
    joi = models.IntegerField()
    empathy = models.IntegerField()
    thoughtfulness = models.IntegerField()

    # @classmethod
    # def create(cls, user, reviewed_object, joi, empathy, thoughtfulness):
    #     review = cls(user, reviewed_object, joi, empathy, thoughtfulness)
    #     return review
