from django.test import TestCase
from django.urls import reverse
from userapp.models import CustomUser


class SavedProductsPageTestCase(TestCase):
    def test_saved_products_returns_200_when_user_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        user_login = self.client.force_login(user)
        response = self.client.get(reverse("saved_products"))
        self.assertEqual(response.status_code, 200)

    def test_saved_products_returns_302_when_user_not_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        response = self.client.get(reverse("saved_products"))
        self.assertEqual(response.status_code, 302)
