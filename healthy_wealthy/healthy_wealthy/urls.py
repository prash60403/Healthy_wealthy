from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Healthy Wealthy Backend Running Successfully 🚀")


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),

    path('api/profile/', include('profiles.urls')),
]