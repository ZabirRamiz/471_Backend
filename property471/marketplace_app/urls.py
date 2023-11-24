from django.urls import path
from . import views

urlpatterns = [
    path("add_to_marketplace", views.add_to_marketplace)
]
