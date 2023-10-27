from django.urls import path 
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),             
    path('logout', views.logout),             
    # path('signup', views.signupView.as_view())
]
