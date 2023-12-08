from rest_framework import serializers
from .models import property
from signup_login_app.serializers import userSerializer

# from payment_app.serializers import adminearningSerializer


class propertySerializer(serializers.ModelSerializer):
    class Meta:
        model = property
        fields = "__all__"
