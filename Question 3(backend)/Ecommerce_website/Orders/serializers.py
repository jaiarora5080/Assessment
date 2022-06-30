from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
     class Meta:
        model = OrderDetails
        fields = ('User_id','Product_id','Product_quantity')

class OrderSerializerToGet(serializers.ModelSerializer):
     class Meta:
        model = OrderDetails
        fields = '__all__'  