from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from profiles.models import UserProfile


class Command(BaseCommand):
    help = 'Create/update a superuser and ensure an attached UserProfile exists.'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--email', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        user_model = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']

        if user_model.objects.filter(username=username).exists():
            user = user_model.objects.get(username=username)
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.WARNING(f'Updated existing superuser: {username}'))
        elif user_model.objects.filter(email=email).exists():
            raise CommandError('A user with this email already exists under a different username.')
        else:
            user = user_model.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(self.style.SUCCESS(f'Created superuser: {username}'))

        profile, created = UserProfile.objects.get_or_create(
            user=user,
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

        if created:
            self.stdout.write(self.style.SUCCESS('Created profile for superuser.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser profile already exists.'))
