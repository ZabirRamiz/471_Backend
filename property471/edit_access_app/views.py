from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.contrib import messages
from datetime import datetime, timedelta

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .models import *
from .serializers import *
from signup_login_app.models import user
from signup_login_app.models import employee


# Create your views here.

# Users can edit their info ( for buyers and sellers )


@api_view(["POST"])
def user_edit(request):
    info = user.objects.get(user_id=request.data["user_id"])

    old_dic = {
        "name": info.name,
        "password": info.password,
        "email": info.email,
        "address": info.address,
        "phone": info.phone,
    }

    new_dic = {
        "name": request.data["name"],
        "password": request.data["password"],
        "email": request.data["email"],
        "address": request.data["address"],
        "phone": request.data["phone"],
    }

    attributes_to_check = ["name", "password", "email", "address", "phone"]

    for attribute in attributes_to_check:
        if new_dic[f"{attribute}"] == "":
            setattr(info, attribute, old_dic[f"{attribute}"])
        else:
            setattr(info, attribute, new_dic[f"{attribute}"])

    user.save(info)

    return JsonResponse({"message": "edit success"}, status=201)
