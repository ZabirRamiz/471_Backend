from django.urls import path 
from . import views

urlpatterns = [
    path('create_property', views.create_property),
]
