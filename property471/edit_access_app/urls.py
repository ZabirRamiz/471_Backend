from django.urls import path
from . import views
urlpatterns = [
    path('user_edit', views.user_edit),
    path('employee_edit',views.employee_edit)
]
