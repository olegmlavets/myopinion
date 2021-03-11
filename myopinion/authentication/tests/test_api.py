import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User


class AuthenticationApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testusername', email='email@test.com', password='testpassword')

    def test_create(self):
        url = reverse('register')

        data = {
            "email": "newemail@test.com",
            "username": "newtestusername",
            "password": "password"
        }

        json_data = json.dumps(data)
        response = self.client.post(path=url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(User.objects.last().email, data['email'])
        self.assertEqual(User.objects.last().username, data['username'])
        # self.assertEqual(User.objects.last().profile, Profile.objects.last())

    def test_verify(self):
        self.assertEqual(self.user.is_verified, False)
        token: object = RefreshToken().for_user(self.user).access_token
        relative_link: str = reverse('email-verify')

        absurl = f'http://localhost{relative_link}?token={token}'
        response = self.client.get(absurl)
        print(response.status_code)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.user.refresh_from_db()
        self.assertEqual(self.user.is_verified, True)
