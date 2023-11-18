from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def user_data(request):
    all_users = user.objects.all()

    all_users_Serialzer = userSerializer(all_users, many=True)

    return JsonResponse({'message': 'This contains all the data of the user table', 'data': all_users_Serialzer.data}, safe=False)


@api_view(['GET'])
def property_data(request):
    all_properties = property.objects.all()

    all_properties_Serializer = propertySerializer(all_properties, many=True)

    return JsonResponse({'message': 'This contains all the data of the property table', 'data': all_properties_Serializer.data}, safe=False)


@api_view(['GET'])
def employee_data(request):
    all_employees = employee.objects.all()

    all_employees_Serializer = employeeSerializer(all_employees, many=True)

    return JsonResponse({'message': 'This contains all the data of the employee table', 'data': all_employees_Serializer.data}, safe=False)


@api_view(['GET'])
def only_user_data(request):
    only_users = user.objects.filter(type = 'user')

    only_users_Serialzer = userSerializer(only_users, many=True)

    return JsonResponse({'message': 'This contains only the data of the users in the table', 'data': only_users_Serialzer.data}, safe=False)

@api_view(['GET'])
def only_agent_data(request):
    pass
@api_view(['GET'])
def only_support_data(request):
    pass
@api_view(['GET'])
def only_agent_data(request):
    pass

@api_view(['POST'])
def user_property(request):
    user_properties = property.objects.filter(user_id = f"{request.data['user_id']}")

    user_properties_Serializer = propertySerializer(user_properties, many = True)

    return JsonResponse({'message': 'This returns all the properties of the user', 'data': user_properties_Serializer.data}, safe = False)