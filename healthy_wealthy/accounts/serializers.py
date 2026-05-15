from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone',
            'password',
        ]

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('A user with this email already exists.')
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            password=validated_data['password'],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not password:
            raise serializers.ValidationError('Password is required.')

        if not username and not email:
            raise serializers.ValidationError('Provide username or email.')

        if email and not username:
            user_obj = User.objects.filter(email__iexact=email).first()
            username = user_obj.username if user_obj else None

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials.')

        data['user'] = user
        return data