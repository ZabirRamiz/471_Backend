from django.urls import path
from . import views

urlpatterns = [
    path("remove_employee", views.remove_employee),
    path("remove_property", views.remove_property),
    path("delete_employee", views.delete_employee),
    path("delete_user", views.delete_user),
]
