from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .serializers import UserSerializer

from django.test import Client
#from .models import User

class CreateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}
        
    def test_can_create_user(self):
        
        response = User.objects.count()
        self.assertEqual(response,1)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GetZones(APITestCase):
    def setUp(self):
        self.c = Client()

    def test_get_zones(self):
        response = self.c.get('/opcapi/zones/')
        #response.status_code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
