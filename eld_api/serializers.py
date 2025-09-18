from rest_framework import serializers
from .models import DriverInfo

class DriverInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverInfo
        fields = '__all__'