# tests/test_views.py
from django.test import TestCase
from ..models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)

        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Burger", price=50, inventory=200)

    def test_getall(self):
        response = self.client.get(reverse('menu'))  
        expected_data = [
            {"id": 2, "title": "IceCream", "price": '80.00', "inventory": 100},
            {"id": 3, "title": "Burger", "price": '50.00', "inventory": 200},
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
