from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [
            "user_id",
            "password",
            "type",
            "name",
            "email",
            "address",
            "phone",
            "session_id",
            "user_image",
            "user_image_path"
        ]


class sessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = session
        fields = ["session_id", "user_id", "status"]


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = [
            "employee_id",
            "password",
            "type",
            "name",
            "email",
            "address",
            "phone",
        ]
