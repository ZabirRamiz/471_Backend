from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerializer):
    class Meta():
        model = user
        fields = ['user_id','password','type','name','email','address','phone']

class sessionSerializer(serializers.ModelSerializer):
    class Meta():
        model = session
        fields = ['user_id', 'status']