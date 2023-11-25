from django.urls import path
from . import views

urlpatterns = [
    path("add_to_marketplace", views.add_to_marketplace),
    path("remove_from_marketplace", views.remove_from_marketplace),
    path("marketplace_properties", views.marketplace_properties),
]
