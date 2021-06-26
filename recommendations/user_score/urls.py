from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_next_object, name='object'),
]