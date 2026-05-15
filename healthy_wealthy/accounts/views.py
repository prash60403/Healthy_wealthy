from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'success': True,
                        'message': 'User registered successfully',
                        'data': serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {
                    'success': False,
                    'errors': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except IntegrityError as exc:
            return Response(
                {
                    'success': False,
                    'message': 'Database integrity error',
                    'error': str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    'success': True,
                    'message': 'Login successful',
                    'data': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                'success': False,
                'errors': serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )