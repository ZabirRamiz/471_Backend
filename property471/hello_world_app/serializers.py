from rest_framework import serializers
from .models import hello_world_model

class hello_worldSerializer(serializers.ModelSerializer):
    class Meta():
        model = hello_world_model
        fields = ['hello', 'world']