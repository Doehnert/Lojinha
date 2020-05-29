from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_cpf_successful(self):
        '''Test creating a new user with username is successful'''
        username = '052.656.179-30'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
