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
@api_view(["POST"])
def remove_employee(request):
    property_val = property.objects.get(property_id=f"{request.data['property_id']}")

    employee_id = request.data["employee_id"]
    if "agent" in employee_id:
        property_val.agent_id = None
    elif "support" in employee_id:
        property_val.support_id = None

    property.save(property_val)
    property_val = property.objects.get(property_id=f"{request.data['property_id']}")
    property_Serializer = propertySerializer(property_val)
    return JsonResponse(
        {
            "message": f"employee - {employee_id} removed from property - {request.data['property_id']}",
            "data": property_Serializer.data,
        },
        status=201,
    )



@api_view(["POST"])
def remove_property(request):
    property_val = property.objects.get(property_id = f"{request.data['property_id']}")

    if property_val.agent_id != None or property_val.support_id != None: 
        property_Serializer = propertySerializer(property_val)
        return JsonResponse({'message': 'remove employee(s) to remove property', 'data': property_Serializer.data}, status = 402)

    property_val.delete()

    return JsonResponse({'message': f"successfully removed property - {request.data['property_id']}"}, status = 201)