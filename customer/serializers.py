from rest_framework import serializers

from .models import  Customer
from hr.models import Engineer
class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


