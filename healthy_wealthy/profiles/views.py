from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer


# CREATE PROFILE (Home Section)
class CreateUserProfileView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# GET PROFILE + UPDATE PROFILE (Profile Section)
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(
            user=self.request.user
        )
        return profile