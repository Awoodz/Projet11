from django.test import TestCase
from django.urls import reverse


class SearchHelpPageTestCase(TestCase):
    def test_search_help_returns_200(self):
        response = self.client.get(reverse("search_help"), {"query": "fa",})
        self.assertEqual(response.status_code, 200)
