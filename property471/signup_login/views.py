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


def createUser(n):
    s = ("user_" + str(n))
    existing_user = 'select user_id from signup_login_user order by user_id asc'
    user_tuple = ''
    with connection.cursor() as cursor:
        cursor.execute(existing_user)
        user_tuple = list(cursor.fetchall())

    if (s,) in user_tuple:
        s = createUser(n+1)
        return s

    else:
        return "user_"+str(n)

# to make it more full proof- take id as argument and change using pk=id 
def sessionInfo():
    session_val = session.objects.order_by('-id').first()
    session_Serializer = sessionSerializer(session_val)
    return JsonResponse(session_Serializer.data, safe=False)



# to make it more full proof- take id as argument and change using pk=id 
def setLogin(user_id):
    session_val = session()

    session_val.user_id_id = user_id
    session_val.status = 'True'
    
    session.save(session_val)
    sessionInfo()



# to make it more full proof- take id as argument and change using pk=id 
def setLogout():
    session_val = session.objects.order_by('-id').first()
    session_val.status = 'False'
    session.save(session_val)


def checkpassword(user_id, password):
    og_password = user.objects.get(user_id=f"{user_id}").password

    if password == og_password:
        return True

    return False


@api_view(["POST"])
def signup(request):
    user_val = user()
    entries = len(user.objects.filter(user_id__startswith='user'))+1

    user_val.user_id = createUser(entries)
    user_val.name = request.data['name']
    user_val.password = request.data['password']
    user_val.email = request.data['email']
    user_val.address = request.data['address']
    user_val.phone = request.data['phone']

    user.save(user_val)
    setLogin(user_val.user_id)
    return JsonResponse({'status': 'Signup Success'}, status=201)


@api_view(["PUT"])
def logout(request):
    setLogout()
    return JsonResponse({'status': 'Logout Success'}, status=201)


@api_view(["PUT"])
def login(request):
    user_id = request.data['user_id']
    password = request.data['password']

    if checkpassword(user_id, password):
        setLogin(user_id)
        return JsonResponse({'status': 'Login Success'}, status=201)

    return JsonResponse({'status': 'Login Failed'}, status=400)
