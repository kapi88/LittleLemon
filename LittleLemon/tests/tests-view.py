from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from api.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(name='Menu 1', price=10.99)
        Menu.objects.create(name='Menu 2', price=15.99)
        
    def test_getall(self):
        response = self.client.get('/api/menus/')  # Adjust the URL according to your project's URL structure
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)