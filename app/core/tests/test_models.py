from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = "test@huntabyte.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        email = "test@HUNTABYTE.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_super_user(
            "test@huntabyte.com", "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
