from django.contrib import admin
from django.utils.html import escape
import os
# Register your models here.

from .models import MuseumObject


@admin.register(MuseumObject)
class MuseumObjectAdmin(admin.ModelAdmin):
    list_display = ('inventory_num', 'title')
    readonly_fields= ('image_tag',)

    
