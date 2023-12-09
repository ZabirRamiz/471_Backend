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
def has_money(property_id, employee_id):
    property_val = property.objects.get(property_id=property_id)
    employer_val = user.objects.get(user_id=property_val.user_id_id)
    employee_val = employee.objects.get(employee_id_id=employee_id)
    user_employee_val = user.objects.get(user_id=employee_id)
    if float(property_val.user_id.wallet) < float(employee_val.hiring_price):
        return False
    else:
        employer_val.wallet = float(employer_val.wallet) - float(
            employee_val.hiring_price
        )
        employee_val.wallet = float(employee_val.wallet) + float(
            employee_val.hiring_price
        )
        user_employee_val.wallet = float(employee_val.wallet)

        property_val.save()
        employer_val.save()
        employee_val.save()
        user_employee_val.save()

        return True


def set_employee(employee_id):
    employee_instance = employee.objects.get(employee_id_id=employee_id)

    return employee_instance


@api_view(["POST"])
def hire_agent(request):
    property_id = request.data["property_id"]
    agent_id = request.data["agent_id"]

    if has_money(property_id, agent_id):
        property_val = property.objects.get(property_id=property_id)

        property_val.agent_id = set_employee(agent_id)
        property.save(property_val)
        property_Serializer = propertySerializer(property_val)
        return JsonResponse(
            {"message": "Successfully Hired Agent", "data": property_Serializer.data},
            status=201,
        )
    return JsonResponse({"message": "lacking sufficient funds"}, status=202)


@api_view(["POST"])
def hire_support(request):
    property_id = request.data["property_id"]
    support_id = request.data["support_id"]
    if has_money(property_id, support_id):
        property_val = property.objects.get(property_id=property_id)

        property_val.support_id = set_employee(support_id)
        property.save(property_val)

        property_Serializer = propertySerializer(property_val)
        return JsonResponse(
            {"message": "Successfully Hired Support", "data": property_Serializer.data},
            status=201,
        )
    return JsonResponse({"message": "lacking sufficient funds"}, status=202)
