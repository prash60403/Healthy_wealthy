from django.urls import path
from .views import CreateUserProfileView, UserProfileView

urlpatterns = [
    path('create/', CreateUserProfileView.as_view(), name='create-profile'),

    path('me/', UserProfileView.as_view(), name='my-profile'),
]