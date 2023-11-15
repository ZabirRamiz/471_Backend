from django.urls import path
from . import views
urlpatterns = [
    path('user_edit', views.user_edit)
]
