from django.urls import path 
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),             
    path('logout', views.logout),    
    path('create_employee',views.create_employee),  
]
