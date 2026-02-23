from rest_framework import serializers
from .models import DeviceType, AlertType, WarningType

class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'

class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = '__all__'

class WarningTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningType
        fields = '__all__'