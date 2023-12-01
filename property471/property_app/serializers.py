from rest_framework import serializers
from .models import *


class propertySerializer(serializers.ModelSerializer):

    class Meta():
        model = property
        fields = "__all__"