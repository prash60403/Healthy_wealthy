from rest_framework import serializers
from .models import DailyTracking

class DailyTrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyTracking
        fields = '__all__'