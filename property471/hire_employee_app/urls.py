from django.urls import path 
from . import views

urlpatterns = [
    path("hire_agent", views.hire_agent),
    path("hire_support", views.hire_support)
]
