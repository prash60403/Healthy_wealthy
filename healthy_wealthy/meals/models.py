from django.db import models

class MealCategory(models.Model):

    CATEGORY_CHOICES = (
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('balanced', 'Balanced'),
        ('keto', 'Keto'),
        ('vegan', 'Vegan'),
    )

    name = models.CharField(max_length=100)

    category_type = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    description = models.TextField()

    def __str__(self):
        return self.name