from rest_framework import serializers
from .models import *
from payment_app.serializers import transactionSerializer


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
