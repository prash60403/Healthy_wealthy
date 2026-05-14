from django.db import models
from meals.models import MealCategory
# Create your models here.
from accounts.models import User

class DietPlan(models.Model):

    PLAN_STATUS = (
        ('active', 'Active'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='diet_plans'
    )

    meals = models.ManyToManyField(MealCategory)

    total_calories = models.IntegerField()

    duration_days = models.IntegerField()

    status = models.CharField(max_length=20, choices=PLAN_STATUS)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Diet Plan"