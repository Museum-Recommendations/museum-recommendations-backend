from django.urls import path
from recommendations import settings

from . import views

urlpatterns = [
    path('', views.get_object_info, name='object'),
    path('<str:inventory_num>', views.get_object_info, name='object'),
    path('image/<str:inventory_num>', views.get_object_photo, name='image'),
] 