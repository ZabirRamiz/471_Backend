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


def createProperty(entries):
    s = ("property_" + str(entries))
    existing_property = "select property_id from property_app_property order by property_id asc"
    property_tuple = ''
    with connection.cursor() as cursor:
        cursor.execute(existing_property)
        property_tuple = list(cursor.fetchall())

    if (s,) in property_tuple:
        s = createProperty(entries+1)
        return s

    else:
        return "property_"+str(entries)

  


@api_view(["POST"])
def create_property(request):
    property_val = property()
    entries = len(property.objects.filter(property_id__startswith='property'))+1


    property_val.property_id = createProperty(entries)
    
