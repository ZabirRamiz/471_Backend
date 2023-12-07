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


@api_view(["GET"])
def user_data(request):
    all_users = user.objects.all()

    all_users_Serialzer = userSerializer(all_users, many=True)

    return JsonResponse(
        {
            "message": "This contains all the data of the user table",
            "data": all_users_Serialzer.data,
        },
        safe=False,
    )


@api_view(["GET"])
def property_data(request):
    all_properties = property.objects.all()

    all_properties_Serializer = propertySerializer(all_properties, many=True)

    return JsonResponse(
        {
            "message": "This contains all the data of the property table",
            "data": all_properties_Serializer.data,
        },
        safe=False,
    )


@api_view(["GET"])
def employee_data(request):
    all_employees = employee.objects.all()

    all_employees_Serializer = employeeSerializer(all_employees, many=True)

    return JsonResponse(
        {
            "message": "This contains all the data of the employee table",
            "data": all_employees_Serializer.data,
        },
        safe=False,
    )


@api_view(["GET"])
def only_user_data(request):
    only_users = user.objects.filter(type="user")

    only_users_Serialzer = userSerializer(only_users, many=True)

    return JsonResponse(
        {
            "message": "This contains all the data of the users with type = 'user' in the table",
            "data": only_users_Serialzer.data,
        },
        safe=False,
    )


@api_view(["GET"])
def only_agent_data(request):
    pass


@api_view(["GET"])
def only_support_data(request):
    pass


@api_view(["GET"])
def only_agent_data(request):
    pass


@api_view(["POST"])
def user_property(request):
    user_properties = property.objects.filter(user_id=f"{request.data['user_id']}")

    user_properties_Serializer = propertySerializer(user_properties, many=True)

    return JsonResponse(
        {
            "message": f"This returns all the properties of the user: {request.data['user_id']}",
            "data": user_properties_Serializer.data,
        },
        safe=False,
    )


@api_view(["POST"])
def agent_property(request):
    agent_properties = property.objects.filter(agent_id=f"{request.data['agent_id']}")

    agent_properties_Serializer = propertySerializer(agent_properties, many=True)

    return JsonResponse(
        {
            "message": f"This returns all the properties of the agent: {request.data['agent_id']}",
            "data": agent_properties_Serializer.data,
        },
        safe=False,
    )


@api_view(["POST"])
def single_user(request):
    single_user = user.objects.get(user_id=f"{request.data['user_id']}")
    single_user_Serializer = userSerializer(single_user)

    return JsonResponse(
        {
            "message": f"This returns all the info of the user: {request.data['user_id']}",
            "data": single_user_Serializer.data,
        },
        safe=False,
    )


@api_view(["POST"])
def single_property(request):
    single_property = property.objects.get(property_id=f"{request.data['property_id']}")
    single_property_Serializer = propertySerializer(single_property)

    return JsonResponse(
        {
            "message": f"This returns all the info of the property: {request.data['property_id']}",
            "data": single_property_Serializer.data,
        },
        safe=False,
    )


@api_view(["POST"])
def single_employee(request):
    single_employee = employee.objects.get(
        employee_id_id=f"{request.data['employee_id']}"
    )
    single_employee_Serializer = employeeSerializer(single_employee)

    return JsonResponse(
        {
            "message": f"This returns all the info of the employee: {request.data['employee_id']}",
            "data": single_employee_Serializer.data,
        },
        safe=False,
    )


@api_view(["GET"])
def needs_admin_approval(request):
    property_val = property.objects.filter(admin_approval="False")
    property_Serializer = propertySerializer(property_val, many=True)
    return JsonResponse(
        {
            "message": "returns all the properties with admin approval false",
            "data": property_Serializer.data,
        }
    )


@api_view(["GET"])
def all_transaction(request):
    transaction_val = transaction.objects.all()

    all_transaction_Serializer = transactionSerializer(transaction_val, many=True)

    return JsonResponse(
        {
            "message": "This returns all the rows of transaction table",
            "data": all_transaction_Serializer.data,
        },
        status=201,
    )
