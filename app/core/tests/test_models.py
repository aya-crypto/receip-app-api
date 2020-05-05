from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """docstring for ModelTests."""
    def test_create_user_with_email_successful(self):
        "test create a new user with an email"
        email ="test@gmail.com"
        password ="tests123"
        user = get_user_model().objects.create_user(
            email = email,
            password =password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """test the email for a new user is normalized"""
        email ='test@GMAIL.COM'
        user =get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises up"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')


    def test_create_new_superuser(self):
        user =get_user_model().objects.create_superuser(
            "test@gmail.com",
            "tests123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
