from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

LOGIN_URL = reverse('login')
LOGOUT_URL = reverse('logout')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class AuthApiTests(TestCase):
    """Test the login & register API (Intergration Test)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@funnymovie.com',
            'password': 'testpass',
        }
        res = self.client.post(LOGIN_URL, payload)
        resp_data = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        email = resp_data.get("user", {}).get("email")
        # Test user is saved to database
        user = get_user_model().objects.get(email=email)
        # Test created user has the same password with payload
        self.assertTrue(user.check_password(payload['password']))
    
    def test_login_user_success(self):
        """Test login user with existed user success"""
        payload = {
            'email': 'test@funnymovie.com',
            'password': 'testpass',
        }
        create_user(**payload)
        res = self.client.post(LOGIN_URL, payload)
        resp_data = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        email = resp_data.get("user", {}).get("email")
        self.assertEqual(email, payload["email"])

    def test_login_user_failed_with_wrong_password(self):
        """Test login user with existed user success"""
        payload = {
            'email': 'test@funnymovie.com',
            'password': 'testpass',
        }
        create_user(**payload)
        payload.update(password='1')
        res = self.client.post(LOGIN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_logout_user_success(self):
        """Test logout success f"""
        payload = {
            'email': 'test@funnymovie.com',
            'password': 'testpass',
        }
        create_user(**payload)
        self.client.post(LOGIN_URL, payload)
        res = self.client.get(LOGOUT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_302_FOUND)
