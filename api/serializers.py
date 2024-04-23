from rest_framework import serializers
from .models import Rabbit

class RabbitSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = Rabbit
        fields = '__all__'