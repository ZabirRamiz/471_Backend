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
from payment_app.views import admin_earning_history

# Create your views here.


def createProperty(entries):
    s = "property_" + str(entries)
    existing_property = (
        "select property_id from property_app_property order by property_id asc"
    )
    property_tuple = ""
    with connection.cursor() as cursor:
        cursor.execute(existing_property)
        property_tuple = list(cursor.fetchall())

    if (s,) in property_tuple:
        s = createProperty(entries + 1)
        return s

    else:
        return "property_" + str(entries)


def assign_owner(user_id):
    user_instance = user.objects.get(user_id=user_id)

    return user_instance


@api_view(["POST"])
def create_property(request):
    property_val = property()
    entries = len(property.objects.filter(property_id__startswith="property")) + 1

    user_id = request.data["user_id"]
    print(user_id)
    user_val = user.objects.get(user_id=f"{user_id}")

    property_val.property_id = createProperty(entries)
    property_val.user_id = assign_owner(user_id)
    property_val.property_location = request.data["property_location"]
    property_val.property_size = request.data["property_size"]
    property_val.property_name = request.data["property_name"]
    property_val.property_price = request.data["property_price"]

    platform_fee = float(request.data["property_price"]) * 0.05

    if float(platform_fee) < float(user_val.wallet):
        print(user_val.wallet)
        user_val.wallet = float(user_val.wallet) - platform_fee
        print(user_val.wallet)

        admin_earning_property_id = property_val.property_id
        admin_earning_user_id = user_id
        admin_earning_earning_amount = platform_fee
        admin_earning_earning_from = "Platform Fee 5%"

        property_val.save()
        user_val.save()
        property_Serializer = propertySerializer(property_val)

        adminearning_Serializer = admin_earning_history(
            admin_earning_property_id,
            admin_earning_user_id,
            admin_earning_earning_amount,
            admin_earning_earning_from,
        )
        return JsonResponse(
            {
                "message": "Property Created",
                "data": property_Serializer.data,
                "adming_earning_data": adminearning_Serializer.data,
            },
            status=201,
        )
    else:
        return JsonResponse({"message": "Insufficient Funds"}, status=202)
