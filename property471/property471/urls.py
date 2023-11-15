"""
URL configuration for property471 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# import the ViewSets
from hello_world_app.views import hello_worldViewSet

router = DefaultRouter()

"""
 register each ViewSet with new 
 router.register('url_name',ViewSet_name) 
 each time
"""
router.register('hello_worldViewSet_url', hello_worldViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # ViewSet paths
    path('hello_world_api/', include(router.urls)),
    # function paths
    path('hello_world_function/',include('hello_world_app.urls')),
    # original backend paths
    path('api/signup_login/', include('signup_login_app.urls')),
    path('api/property/', include('property_app.urls')),
    path('api/hire_employee/', include('hire_employee_app.urls')),
    # path('api/get_data/', include('get_data_app.urls')),

]
