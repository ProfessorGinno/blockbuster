from django.test import TestCase, Client
from django.contrib.auth.models import User


class LoginUserTestCase(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test.user',
            'password': 'temp123'
        }

        self.credentials_superuser = {
            "username":'admin123',
            "password":"test123"
        }
        User.objects.create_user(**self.credentials)
        User.objects.create_superuser(**self.credentials_superuser)
        self.client = Client()

    def test_login_user(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_superuser(self):
        response = self.client.post('/admin/', self.credentials_superuser, follow=True)
        self.assertEqual(response.status_code, 200)

class SignUpUserTestCase(TestCase):
    def setUp(self):
        self.data
