from django.test import TestCase, Client
from django.contrib.auth.models import User


class AccountTestCase(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test.user',
            'password': 'temp123'
        }

        self.credentials_superuser = {
            "username":'admin123',
            "password":"test123"
        }
        self.user = User.objects.create_user(**self.credentials)
        self.superuser = User.objects.create_superuser(**self.credentials_superuser)
        self.client = Client()

    def test_login_user(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_superuser(self):
        response = self.client.post('/admin/', self.credentials_superuser, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_wrong_username(self):
        response = self.client.post('/admin/', {'username':'wrong', 'password':'temp123'})
        self.assertFalse(response.get('authenticated'))

    def test_wrong_password(self):
        response = self.client.post('/admin/', {'username':'test.user', 'password':'wrong'})
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        self.user.delete()