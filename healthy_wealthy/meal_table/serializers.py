from rest_framework import serializers
from .models import Meal


class MealTableSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Meal

        fields = '__all__'