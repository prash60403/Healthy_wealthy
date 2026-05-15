from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class AccountsAPITests(APITestCase):
    def setUp(self):
        self.register_url = '/api/accounts/register/'
        self.login_url = '/api/accounts/login/'

    def test_register_returns_user_data_without_password(self):
        payload = {
            'username': 'sana',
            'email': 'sana@example.com',
            'phone': '1234567890',
            'password': 'StrongPass123!',
        }

        response = self.client.post(self.register_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['username'], payload['username'])
        self.assertEqual(response.data['data']['email'], payload['email'])
        self.assertNotIn('password', response.data['data'])

    def test_login_authenticates_with_username_and_returns_tokens(self):
        user = User.objects.create_user(
            username='alex',
            email='alex@example.com',
            password='StrongPass123!',
        )

        payload = {
            'username': user.username,
            'password': 'StrongPass123!',
        }

        response = self.client.post(self.login_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertIn('access_token', response.data['data'])
        self.assertIn('refresh_token', response.data['data'])

    def test_login_authenticates_with_email_and_password(self):
        user = User.objects.create_user(
            username='maya',
            email='maya@example.com',
            password='StrongPass123!',
        )

        payload = {
            'email': user.email,
            'password': 'StrongPass123!',
        }

        response = self.client.post(self.login_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['username'], user.username)

    def test_login_fails_on_invalid_credentials(self):
        User.objects.create_user(
            username='john',
            email='john@example.com',
            password='StrongPass123!',
        )

        payload = {
            'username': 'john',
            'password': 'WrongPass999!',
        }

        response = self.client.post(self.login_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])