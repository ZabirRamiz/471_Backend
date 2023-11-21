from django.urls import path
from . import views

urlpatterns = [
    path("user_data", views.user_data),
    path("employee_data", views.employee_data),
    path("property_data", views.property_data),
    path("only_user_data", views.only_user_data),
    path("only_agent_data", views.only_agent_data),
    path("only_support_data", views.only_support_data),
    path("user_property", views.user_property),
    path("single_user", views.single_user),
]
