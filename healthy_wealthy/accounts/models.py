from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username