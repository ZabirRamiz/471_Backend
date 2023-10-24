from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import hello_world_model
from .serializers import hello_worldSerializer
# Create your views here.
class hello_worldViewSet(viewsets.ModelViewSet):
    queryset = hello_world_model.objects.all()
    serializer_class = hello_worldSerializer

@api_view(['Get','POST'])
def first_function(request):
    if request.method == "POST":
        query = hello_world_model.objects.filter(hello = request.data['hello'])
        serializer = hello_worldSerializer(query, many = True)
        out = serializer.data
        return JsonResponse(out, safe = False)
    
    elif request.method == "GET":
        query = hello_world_model.objects.all()
        serializer = hello_worldSerializer(query, many = True)
        out = serializer.data
        return JsonResponse(out, safe = False)
        