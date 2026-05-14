from rest_framework import serializers
from .models import BodyAnalysis


class BodyAnalysisSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = BodyAnalysis

        fields = '__all__'