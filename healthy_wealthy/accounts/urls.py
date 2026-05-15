from django.urls import path

from .views import LoginView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # Temporary backward-compatible alias for clients using a misspelled route.
    path('reqgister/', RegisterView.as_view(), name='register_alias'),
    path('login/', LoginView.as_view(), name='login'),
]
