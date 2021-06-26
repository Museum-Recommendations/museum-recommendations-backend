from django.contrib import admin

# Register your models here.

from .models import MuseumObject


@admin.register(MuseumObject)
class MuseumObjectAdmin(admin.ModelAdmin):
	pass
	
