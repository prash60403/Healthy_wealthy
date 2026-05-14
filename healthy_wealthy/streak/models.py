from django.db import models

from accounts.models import User
class UserStreak(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    current_streak = models.IntegerField(default=0)

    highest_streak = models.IntegerField(default=0)

    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username