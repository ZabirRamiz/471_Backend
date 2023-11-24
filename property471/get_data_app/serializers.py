from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"


class propertySerializer(serializers.ModelSerializer):
    class Meta:
        model = property
        fields = "__all__"
