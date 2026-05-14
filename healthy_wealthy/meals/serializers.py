from rest_framework import serializers
from .models import MealCategory

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealCategory
        fields = '__all__'