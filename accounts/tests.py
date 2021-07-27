from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from copy import copy
from rest_framework.authtoken.models import Token


user_model = get_user_model()
test_user = {'username': 'test_user',
             'email': 'user@email.com',
             'password': 'my_awesome_password_42'}


class TestAccounts(APITestCase):
    def test_user_create(self):
        """
        Ensure we can create a new user
        """
        url = reverse('accounts:register')
        data = copy(test_user)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user_model.objects.count(), 1)
        self.assertEqual(user_model.objects.get().email, 'user@email.com')

    def test_get_token(self):
        """
        Ensure we can get token
        """
        url = reverse('accounts:register')
        data = copy(test_user)

        response = self.client.post(url, data, format='json')

        user = user_model.objects.get()

        url = reverse('accounts:token')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(Token.objects.get(user=user).key, response.data['key'])
