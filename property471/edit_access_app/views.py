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
        "user_image": info.user_image,
        "user_image_path": info.user_image_path,
    }

    try:
        image = request.FILES["user_image"]
    except:
        image = "default"

    if image != "default":
        print("------------------------------")
        print(image)
        image_name = image.name
        image_path = f"/user_image/{image_name}"
    else:
        image_path = ""

    new_dic = {
        "name": request.data["name"],
        "password": request.data["password"],
        "email": request.data["email"],
        "address": request.data["address"],
        "phone": request.data["phone"],
        "user_image": request.data["user_image"],
        "user_image_path": image_path,
    }

    attributes_to_check = [
        "name",
        "password",
        "email",
        "address",
        "phone",
        "user_image",
        "user_image_path",
    ]

    for attribute in attributes_to_check:
        if new_dic[f"{attribute}"] == "":
            setattr(info, attribute, old_dic[f"{attribute}"])
        else:
            setattr(info, attribute, new_dic[f"{attribute}"])

    user.save(info)
    # image_name = request.data['user_image']
    # file_path = r"C:\Users\Zabir\Desktop\BRAC\471\project\471_Backend\property471\media\user_image"
    # full_path = f"{file_path}\{image_name}"
    # print(full_path)
    user_val = user.objects.get(user_id=request.data["user_id"])
    user_Serializer = userSerializer(user_val)

    return JsonResponse(
        {"message": "edit success", "data": user_Serializer.data}, status=201
    )


@api_view(["POST"])
def employee_edit(request):
    info = employee.objects.get(employee_id_id=request.data["user_id"])
    old_dic = {
        "name": info.name,
        "password": info.password,
        "type": info.email,
        "address": info.address,
        "phone": info.phone,
        "email": info.email,
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

    employee.save(info)

    employee_val = employee.objects.get(employee_id_id=f"{request.data['user_id']}")
    employee_Serializer = employeeSerializer(employee_val)

    info = user.objects.get(user_id=request.data["user_id"])
    old_dic = {
        "name": info.name,
        "password": info.password,
        "email": info.email,
        "address": info.address,
        "phone": info.phone,
        "user_image": info.user_image,
        "user_image_path": info.user_image_path,
    }

    try:
        image = request.FILES["user_image"]
    except:
        image = "default"

    if image != "default":
        print("------------------------------")
        print(image)
        image_name = image.name
        image_path = f"/user_image/{image_name}"
    else:
        image_path = ""

    new_dic = {
        "name": request.data["name"],
        "password": request.data["password"],
        "email": request.data["email"],
        "address": request.data["address"],
        "phone": request.data["phone"],
        "user_image": request.data["user_image"],
        "user_image_path": image_path,
    }

    attributes_to_check = [
        "name",
        "password",
        "email",
        "address",
        "phone",
        "user_image",
        "user_image_path",
    ]

    for attribute in attributes_to_check:
        if new_dic[f"{attribute}"] == "":
            setattr(info, attribute, old_dic[f"{attribute}"])
        else:
            setattr(info, attribute, new_dic[f"{attribute}"])

    user.save(info)

    user_val = user.objects.get(user_id=request.data["user_id"])
    user_Serializer = userSerializer(user_val)

    return JsonResponse(
        {
            "message": "edit success",
            "employee_data": employee_Serializer.data,
            "data": user_Serializer.data,
        },
        status=201,
    )
