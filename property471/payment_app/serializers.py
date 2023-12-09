from rest_framework import serializers
from property_app.serializers import propertySerializer
from signup_login_app.serializers import userSerializer, employeeSerializer
from .models import *


class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = "__all__"


class adminearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_earning
        fields = "__all__"
