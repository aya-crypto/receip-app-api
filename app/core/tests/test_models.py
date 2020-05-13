from django.test import TestCase
from django.contrib.auth import get_user_model

from unittest.mock import patch
from core import models


def sample_user(email="test@gmail.com",password='test123'):
    return get_user_model().objects.create_user(email,password)

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

    def test_tag_str(self):
        tag =models.Tag.objects.create(
            user=sample_user(),
            name="vagan"
        )

        self.assertEqual(str(tag),tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)


    def test_recipe_str(self):
        """test the ecipe string representation"""
        recipe = models.Recipe.objects.create(
            user =sample_user(),
            title='steak',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe),recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self,mock_uuid):
        """test that image is saved in correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value =uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path=f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path,exp_path)
