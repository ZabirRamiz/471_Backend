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
from signup_login_app.models import user
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


def assign_owner(owner_id):
    user_instance = user.objects.get(user_id = owner_id)

    return user_instance


@api_view(["POST"])
def create_property(request):
    property_val = property()
    entries = len(property.objects.filter(property_id__startswith='property'))+1
    owner_id = request.data['user_id']


    property_val.property_id = createProperty(entries)
    property_val.owner_id = assign_owner(owner_id)
    property_val.property_location = request.data['property_location']
    property_val.property_size = request.data['property_size']
    property_val.property_name = request.data['property_name']
    property_val.property_price = request.data['property_price']

    property.save(property_val)

    return JsonResponse({'message': 'Property Created'}, status = 201)



    

