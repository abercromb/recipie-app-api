from django.test.testcases import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "email@example.com"
        password = "password123!"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_emails = [
            ["text1@EXM.com", "text1@exm.com"],
            ["TEST@test.com", "TEST@test.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "test123")
            self.assertEqual(user.email, expected)

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "super_user@user.com",
            "passwd123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
