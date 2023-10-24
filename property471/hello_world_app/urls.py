from django.urls import path
from . import views

urlpatterns = [
    path('first_function_url',views.first_function),
]
