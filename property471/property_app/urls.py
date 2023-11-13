from django.urls import path 
from . import views

urlpatterns = [
    path('property', views.property)
]
