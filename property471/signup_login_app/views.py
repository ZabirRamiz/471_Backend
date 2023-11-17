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


def createUser(entries):
    s = ("user_" + str(entries))
    existing_user = "select user_id from signup_login_app_user where type = 'user' order by user_id asc"
    user_tuple = ''
    with connection.cursor() as cursor:
        cursor.execute(existing_user)
        user_tuple = list(cursor.fetchall())

    if (s,) in user_tuple:
        s = createUser(entries+1)
        return s

    else:
        return "user_"+str(entries)


def createAgent(entries):
    s = ("agent_" + str(entries))
    existing_agent = "select user_id from signup_login_app_user where type = 'agent' order by user_id asc"
    agent_tuple = ''
    with connection.cursor() as cursor:
        cursor.execute(existing_agent)
        agent_tuple = list(cursor.fetchall())

    if (s,) in agent_tuple:
        s = createAgent(entries+1)
        return s

    else:
        return "agent_"+str(entries)


def createSupport(entries):
    s = ("support_" + str(entries))
    existing_support = "select user_id from signup_login_app_user where type != 'agent' and type != 'user' order by user_id asc"

    support_tuple = ''
    with connection.cursor() as cursor:
        cursor.execute(existing_support)
        support_tuple = list(cursor.fetchall())

    if (s,) in support_tuple:
        s = createSupport(entries+1)
        return s

    else:
        return "support_"+str(entries)


def sessionInfo(session_id):
    session_val = session.objects.get(session_id=f"{session_id}")
    session_Serializer = sessionSerializer(session_val)
    return JsonResponse(session_Serializer.data, safe=False)


def setLogin(user_id):
    session_val = session()

    session_val.user_id_id = user_id
    session_val.status = 'True'
    session.save(session_val)

    session_id = session.objects.order_by('-session_id').first().session_id
    user_val = user.objects.get(user_id=f'{user_id}')
    user_val.session_id = session_id

    user.save(user_val)

    sessionInfo(session_id)

    user.objects.get(user_id=f'{user_id}')
    user_Serializer = userSerializer(user_val)
    message = 'Login Success'
    return (message, user_Serializer)


def setLogout(user_id):
    session_val = session.objects.filter(
        user_id=f'{user_id}').order_by('-session_id')[0]
    session_val.status = 'False'
    session.save(session_val)


def checkpassword(user_id, password):
    og_password = user.objects.get(user_id=f"{user_id}").password

    if password == og_password:
        return True

    return False


def checkuser(user_id_to_check):
    user_exists = user.objects.filter(user_id=user_id_to_check).exists()

    return user_exists


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

    login_message, user_Serializer = setLogin(user_val.user_id)
    return JsonResponse({'message': 'Signup Success', 'data': user_Serializer.data}, status=201)


@api_view(["POST"])
def logout(request):
    user_id = request.data['user_id']
    setLogout(user_id)
    return JsonResponse({'status': 'Logout Success'}, status=201)


@api_view(["POST"])
def login(request):
    user_id = request.data['user_id']
    password = request.data['password']

    if checkuser(user_id):
        if checkpassword(user_id, password):
            message, user_Serializer = setLogin(user_id)

            return JsonResponse({'message': message, 'data': user_Serializer.data}, status=201)

    return JsonResponse({'error': 'Incorrect Username Or Password'}, status=400)


def create_agent(request):
    agent_val = user()
    entries = len(user.objects.filter(user_id__startswith='agent'))+1

    agent_val.user_id = createAgent(entries)
    agent_val.name = request.data['name']
    agent_val.password = request.data['password']
    agent_val.type = request.data['type']
    agent_val.email = request.data['email']
    agent_val.address = request.data['address']
    agent_val.phone = request.data['phone']

    user.save(agent_val)

    return agent_val.user_id


def create_support(request):
    support_val = user()
    entries = len(user.objects.filter(user_id__startswith='support'))+1

    support_val.user_id = createSupport(entries)
    support_val.name = request.data['name']
    support_val.password = request.data['password']
    support_val.type = request.data['type']
    support_val.email = request.data['email']
    support_val.address = request.data['address']
    support_val.phone = request.data['phone']

    user.save(support_val)

    return support_val.user_id


@api_view(["POST"])
def create_employee(request):
    print(request.data['name'])
    if request.data['type'] == 'agent':
        employee_id = create_agent(request)
    elif request.data['type'] != 'agent':
        employee_id = create_support(request)

    employee_val = employee()

    employee_val.employee_id = employee_id
    employee_val.name = request.data['name']
    employee_val.password = request.data['password']
    employee_val.type = request.data['type']
    employee_val.email = request.data['email']
    employee_val.address = request.data['address']
    employee_val.phone = request.data['phone']

    employee.save(employee_val)

    return JsonResponse({'status': 'Successfully Created Employee'}, status=201)
