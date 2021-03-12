from django.test import TestCase
from authentication.serializers import *

from authentication.models import User


class AuthenticationSerializerTestCase(TestCase):

    def test_register_serializer(self):
        user = User.objects.create(username='testusername', email='email@test.com', password='testpassword')
        serialzier_data = RegisterSerializer(instance=user).data

        exepted_data = {
            "email": "email@test.com",
            "username": "testusername"
        }
        self.assertEqual(serialzier_data, exepted_data)

    def test_wrong_register_serializer(self):
        wrong_data = {
            "email": "wrongemail",
            "username": "testusername",
            "password": "testpassword"

        }
        serialzier_data = RegisterSerializer(data=wrong_data).is_valid()

        exepted_data = False

        self.assertEqual(serialzier_data, exepted_data)
