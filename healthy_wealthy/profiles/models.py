from django.db import models
from accounts.models import User

class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    GOAL_CHOICES = (
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('balanced', 'Balanced'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    height = models.FloatField()
    weight = models.FloatField()

    goal = models.CharField(max_length=30, choices=GOAL_CHOICES)

    allergies = models.TextField(blank=True, null=True)

    activity_level = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username