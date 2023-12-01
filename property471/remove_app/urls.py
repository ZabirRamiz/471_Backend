from django.urls import path
from . import views

urlpatterns = [
    path('remove_employee', views.remove_employee),
    path('remove_property', views.remove_property),
]
