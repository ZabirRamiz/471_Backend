from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerialzer):
    class Meta():
        model = user
        fields = '__all__'