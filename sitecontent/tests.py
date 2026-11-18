from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import SiteProfile


class PublicPageTests(TestCase):
    def test_home_renders_original_content_and_admin_link(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JANNA GENTS HOSTEL")
        self.assertContains(response, 'href="/admin/"')
        self.assertNotContains(response, "editorModal")
        self.assertNotContains(response, "openEditLogin")
        self.assertTrue(SiteProfile.objects.filter(pk=1).exists())

    def test_database_content_updates_are_rendered_on_home(self):
        profile, _ = SiteProfile.objects.get_or_create(pk=1)
        profile.website_name = "Updated Hostel Name"
        profile.phone = "+91 90000 11111"
        profile.save()

        response = self.client.get(reverse("home"))
        self.assertContains(response, "Updated Hostel Name")
        self.assertContains(response, "tel:919000011111")
        self.assertContains(response, "https://wa.me/919000011111")

    def test_admin_is_protected_and_available_to_staff(self):
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

        user = get_user_model().objects.create_superuser(
            username="admin-test", email="admin@example.com", password="safe-test-password"
        )
        self.client.force_login(user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Website Content")
