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
def add_to_marketplace(request):
    property_val = property.objects.get(property_id = request.data['property_id'])

    property_val.market_status = 'for sale'

    property.save(property_val)

    property_Serializer = propertySerializer(property_val)

    return JsonResponse({"message": "updated property status to - for sale", "data": property_Serializer.data}, status = 201)