from rest_framework import serializers
from .models import *


class propertySerializer(serializers.ModelSerializer):

    class Meta():
        model = property
        fields = ['property_id', 'owner_id', 'agent_id', 'support_id', 'market_status',
                  'property_location', 'property_size', 'property_name', 'property_price']
