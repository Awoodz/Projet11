from django.test import TestCase
from django.urls import reverse
from userapp.models import CustomUser


class AccountPageTestCase(TestCase):
    def test_account_returns_200_when_user_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        user_login = self.client.force_login(user)
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 200)

    def test_account_returns_302_when_user_not_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 302)
