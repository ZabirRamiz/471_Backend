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
def ask_approval(request):
    property_val = property.objects.get(property_id=f'{request.data["property_id"]}')
    property_val.admin_approval = "False"
    property.save(property_val)

    property_Serializer = propertySerializer(property_val)
    buyer_val = user.objects.get(user_id=f"{request.data['buyer_id']}")
    buyer_Serializer = userSerializer(buyer_val)
    return JsonResponse(
        {
            "message": "changed admin approval to False",
            "property_data": property_Serializer.data,
            "buyer_data": buyer_Serializer.data,
        },
        status=201,
    )


@api_view(["POST"])
def give_approval(request):
    buyer_id = request.data["buyer_id"]
    property_id = request.data["property_id"]

    property_val = property.objects.get(property_id=property_id)
    seller_id = property_val.user_id.user_id
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    print(seller_id)
    agent_id = property_val.agent_id.employee_id
    print(agent_id)

    seller_val = user.objects.get(user_id=seller_id)
    buyer_val = user.objects.get(user_id=buyer_id)
    agent_val = employee.objects.get(employee_id=agent_id)

    property_val.admin_approval = True
    property_val.user_id.user_id = buyer_id
    property_val.market_status = "Available For Sale"
    property_val.agent_id.employee_id = "NULL"
    property_val.support_id.employee_id = "NULL"

    buyer_val.wallet = int(buyer_val.wallet) - int(property_val.property_price)
    agent_commission = int(property_val.property_price) * float(
        f".0{agent_val.commission}"
    )
    agent_val.wallet = int(agent_val.wallet) + agent_commission
    seller_val = (
        int(seller_val.wallet) + int(property_val.property_price) - agent_commission
    )

    user.save(seller_val)
    user.save(buyer_val)
    employee.save(agent_val)
    property.save(property_val)

    seller_Serializer = userSerializer(seller_val)
    buyer_Serializer = userSerializer(buyer_val)
    agent_Serializer = employeeSerializer(agent_val)
    property_Serializer = propertySerializer(property_val)

    return JsonResponse(
        {
            "message": "set admin approval and handled the payments",
            "property_data": property_Serializer.data,
            "seller_data": seller_Serializer.data,
            "buyer_data": buyer_Serializer.data,
            "agent_data": agent_Serializer.data
        },
        status = 201
    )
