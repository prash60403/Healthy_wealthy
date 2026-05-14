
from django.db import models
from accounts.models import User

class DailyTracking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='daily_tracking'
    )

    consumed_calories = models.IntegerField(default=0)

    burned_calories = models.IntegerField(default=0)

    water_intake = models.FloatField(default=0)

    weight = models.FloatField(null=True, blank=True)

    completed_diet = models.BooleanField(default=False)

    tracking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username