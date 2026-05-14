from django.db import models
from accounts.models import User

class BodyAnalysis(models.Model):

    BODY_TYPE = (
        ('ectomorph', 'Ectomorph'),
        ('mesomorph', 'Mesomorph'),
        ('endomorph', 'Endomorph'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='body_analysis'
    )


    bmi = models.FloatField()

    body_fat_percentage = models.FloatField(null=True, blank=True)

    body_type = models.CharField(max_length=30, choices=BODY_TYPE)

    calories_needed = models.IntegerField()

    protein_needed = models.IntegerField()

    carbs_needed = models.IntegerField()

    fats_needed = models.IntegerField()

    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username