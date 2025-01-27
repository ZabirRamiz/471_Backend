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
def have_money(property_val, buyer_val):
    first_check = float(property_val.property_price)
    admin_receives = first_check * 0.1
    second_check = first_check + float(admin_receives)
    if second_check > float(buyer_val.wallet):
        return False
    return True


def createTransaction(entries):
    s = "transaction_" + str(entries)
    existing_transaction = (
        "select transaction_id from payment_app_transaction order by transaction_id asc"
    )

    transaction_tuple = ""
    with connection.cursor() as cursor:
        cursor.execute(existing_transaction)
        transaction_tuple = list(cursor.fetchall())

    if (s,) in transaction_tuple:
        s = createTransaction(entries + 1)
        return s

    else:
        return "transaction_" + str(entries)


def createEarning(entries):
    s = "earning_" + str(entries)
    existing_earning = (
        "select earning_id from payment_app_admin_earning order by earning_id asc"
    )

    earning_tuple = ""
    with connection.cursor() as cursor:
        cursor.execute(existing_earning)
        earning_tuple = list(cursor.fetchall())

    if (s,) in earning_tuple:
        s = createEarning(entries + 1)
        return s

    else:
        return "earning_" + str(entries)


def admin_earning_history(property_id, user_id, earning_amount, earning_from):
    admin_earning_val = admin_earning()
    entries = len(admin_earning.objects.filter(earning_id__startswith="earning")) + 1

    admin_val = user.objects.get(type="admin")
    admin_val.wallet = float(admin_val.wallet) + earning_amount

    admin_earning_val.earning_id = createEarning(entries)
    admin_earning_val.property_id = property_id
    admin_earning_val.user_id = user_id
    admin_earning_val.earning_amount = earning_amount
    admin_earning_val.earning_from = earning_from

    admin_earning_val.save()
    admin_val.save()
    adminearning_Serializer = adminearningSerializer(admin_earning_val)

    return adminearning_Serializer


def transaction_history(
    buyer_sends,
    seller_receives,
    admin_receives,
    agent_receives,
    agent_id,
    buyer_id,
    property_id,
    seller_id,
):
    transaction_val = transaction()
    entries = (
        len(transaction.objects.filter(transaction_id__startswith="transaction")) + 1
    )

    transaction_val.transaction_id = createTransaction(entries)
    transaction_val.buyer_sends = buyer_sends
    transaction_val.seller_receives = seller_receives
    transaction_val.agent_receives = agent_receives
    transaction_val.admin_receives = admin_receives
    transaction_val.agent_id = agent_id
    transaction_val.buyer_id = buyer_id
    transaction_val.property_id = property_id
    transaction_val.seller_id = seller_id

    transaction_val.save()
    transaction_Serializer = transactionSerializer(transaction_val)
    return transaction_Serializer


@api_view(["POST"])
def ask_approval(request):
    property_val = property.objects.get(property_id=f'{request.data["property_id"]}')
    buyer_val = user.objects.get(user_id=f"{request.data['buyer_id']}")
    if have_money(property_val, buyer_val):
        property_val.admin_approval = "False"
        property_val.buyer_id_id = request.data["buyer_id"]
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
    return JsonResponse({"message": "insufficient funds"}, status=202)


@api_view(["POST"])
def give_approval(request):
    buyer_id = request.data["buyer_id"]
    property_id = request.data["property_id"]

    property_val = property.objects.get(property_id=property_id)

    seller_id = property_val.user_id_id
    agent_id = property_val.agent_id_id

    seller_val = user.objects.get(user_id=seller_id)
    buyer_val = user.objects.get(user_id=buyer_id)
    agent_val = employee.objects.get(employee_id_id=agent_id)

    user_agent_val = user.objects.get(user_id=agent_id)
    if have_money(property_val, buyer_val):
        property_val.admin_approval = True
        property_val.user_id_id = buyer_id
        property_val.market_status = "Available For Sale"
        property_val.agent_id_id = None
        property_val.support_id_id = None
        property_val.buyer_id_id = None

        admin_earning_amount = float(property_val.property_price) * 0.1

        buyer_val.wallet = (
            float(buyer_val.wallet)
            - float(property_val.property_price)
            - admin_earning_amount
        )
        agent_commission = (
            float(property_val.property_price) * float(agent_val.commission) / 100
        )
        agent_val.wallet = float(agent_val.wallet) + agent_commission
        seller_val.wallet = (
            float(seller_val.wallet)
            + float(property_val.property_price)
            - agent_commission
        )

        user_agent_val.wallet = agent_val.wallet
        property_val.admin_approval = None

        transaction_Serializer = transaction_history(
            float(property_val.property_price) + admin_earning_amount,
            float(property_val.property_price) - agent_commission,
            admin_earning_amount,
            agent_commission,
            agent_id,
            buyer_id,
            property_id,
            seller_id,
        )

        adminearning_Serializer = admin_earning_history(
            property_id,
            buyer_id,
            admin_earning_amount,
            "Commission from Transaction 10%",
        )

        seller_val.save()
        buyer_val.save()
        agent_val.save()
        property_val.save()
        user_agent_val.save()

        seller_Serializer = userSerializer(seller_val)
        buyer_Serializer = userSerializer(buyer_val)
        agent_Serializer = employeeSerializer(agent_val)
        property_Serializer = propertySerializer(property_val)

        return JsonResponse(
            {
                "message": "Set admin approval and handled the payments",
                "property_data": property_Serializer.data,
                "seller_data": seller_Serializer.data,
                "buyer_data": buyer_Serializer.data,
                "agent_data": agent_Serializer.data,
                "transaction_data": transaction_Serializer.data,
                "admin_earning_data": adminearning_Serializer.data,
            },
            status=201,
        )
    return JsonResponse({"message": "insufficient funds"}, status=202)


@api_view(["POST"])
def admin_rejects(request):
    property_id = request.data["property_id"]

    property_val = property.objects.get(property_id=f"{property_id}")

    property_val.admin_approval = None
    property_val.buyer_id_id = None

    property_val.save()

    property_Serializer = propertySerializer(property_val)

    return JsonResponse(
        {
            "message": "set admin approval and buyer_id to NULL",
            "data": property_Serializer.data,
        },
        status=201,
    )
