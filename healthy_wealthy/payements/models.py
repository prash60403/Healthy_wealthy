from django.db import models
from accounts.models import User

class Payment(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_id = models.CharField(max_length=255)

    order_id = models.CharField(max_length=255)

    status = models.CharField(max_length=20, choices=PAYMENT_STATUS)

    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id