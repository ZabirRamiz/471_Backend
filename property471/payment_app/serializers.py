from rest_framework import serializers
from property_app.serializers import propertySerializer
from signup_login_app.serializers import userSerializer, employeeSerializer
from .models import transaction


class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = "__all__"
