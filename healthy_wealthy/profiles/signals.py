from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User

from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile_for_superuser(sender, instance, created, **kwargs):
    """Ensure superusers have an associated profile record."""
    if created and instance.is_superuser:
        UserProfile.objects.get_or_create(
            user=instance,
            defaults={
                'age': 30,
                'gender': 'male',
                'height': 170.0,
                'weight': 70.0,
                'goal': 'balanced',
                'activity_level': 'moderate',
                'allergies': '',
            },
        )
