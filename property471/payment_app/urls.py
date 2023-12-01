from django.urls import path
from . import views

urlpatterns = [
    path('ask_approval', views.ask_approval),
    path('give_approval', views.give_approval),
]
