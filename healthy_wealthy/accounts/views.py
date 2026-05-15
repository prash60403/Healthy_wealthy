from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from django.db import IntegrityError

from .serializers import RegisterSerializer
from .serializers import LoginSerializer


class RegisterView(APIView):

    def post(self, request):

        try:

            serializer = RegisterSerializer(data=request.data)

            if serializer.is_valid():

                serializer.save()

                return Response({

                    'success': True,
                    'message': 'User Registered Successfully',
                    'data': serializer.data

                }, status=status.HTTP_201_CREATED)

            return Response({

                'success': False,
                'errors': serializer.errors

            }, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as e:

            return Response({

                'success': False,
                'message': 'Database Integrity Error',
                'error': str(e)

            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:

            return Response({

                'success': False,
                'message': 'Something went wrong during registration',
                'error': str(e)

            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):

    def post(self, request):

        try:

            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid():

                user = serializer.validated_data['user']

                refresh = RefreshToken.for_user(user)

                return Response({

                    'success': True,
                    'message': 'Login Successful',

                    'access_token': str(refresh.access_token),

                    'refresh_token': str(refresh),

                    'username': user.username,

                    'email': user.email

                }, status=status.HTTP_200_OK)

            return Response({

                'success': False,
                'errors': serializer.errors

            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:

            return Response({

                'success': False,
                'message': 'Something went wrong during login',
                'error': str(e)

            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)