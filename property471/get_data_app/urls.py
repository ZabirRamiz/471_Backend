from django.urls import path
from . import views

urlpatterns = [
    # full user/employee/property table data
    path("user_data", views.user_data),
    path("employee_data", views.employee_data),
    path("property_data", views.property_data),
    # all users/agents/supports data from user table
    path("only_user_data", views.only_user_data),
    path("only_agent_data", views.only_agent_data),
    path("only_support_data", views.only_support_data),
    # all user/agent/support specific property data from property table
    path("user_property", views.user_property),
    path("agent_property", views.agent_property),
    # specific user/employee/property data from user/employee/property table
    path("single_user", views.single_user),
    path("single_employee", views.single_employee),
    path("single_property", views.single_property),
    # for payment app
    path("needs_admin_approval", views.needs_admin_approval),
    path("all_transaction", views.all_transaction),
]
