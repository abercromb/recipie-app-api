from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@test.com",
            password="admin123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test_user@test.com",
            password="test123",
            name="Test User"
        )

    def test_list_users(self):
        url = reverse("admin:core_user_changelist")
        result = self.client.get(url)

        self.assertContains(result, self.user.name)
        self.assertContains(result, self.user.email)

    def test_edit_user_page(self):
        url = reverse("admin:core_user_change", args=[self.user.id])
        result = self.client.get(url)

        self.assertEqual(result.status_code, 200)

    def test_create_user_page(self):
        url = reverse("admin:core_user_add")
        result = self.client.get(url)

        self.assertEqual(result.status_code, 200)
