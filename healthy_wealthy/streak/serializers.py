from rest_framework import serializers
from .models import UserStreak

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStreak

        fields = '__all__'