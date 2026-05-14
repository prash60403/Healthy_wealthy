from django.db import models

from meals.models import MealCategory

class Meal(models.Model):

    category = models.ForeignKey(
        MealCategory,
        on_delete=models.CASCADE,
        related_name='meals'
    )

    meal_name = models.CharField(max_length=255)

    description = models.TextField()

    calories = models.IntegerField()

    protein = models.IntegerField()

    carbs = models.IntegerField()

    fats = models.IntegerField()

    image = models.ImageField(upload_to='meal_images/')

    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.meal_name