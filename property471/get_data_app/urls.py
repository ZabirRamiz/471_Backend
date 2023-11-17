from django.urls import path 
from . import views

urlpatterns = [
    path('user_data',views.user_data),
    path('employee_data',views.employee_data),
    path('property_data',views.property_data),
]
