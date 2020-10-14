from django.test import TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class SearchHelpPageTestCase(TestCase):
    def test_search_help_returns_200(self):
        response = self.client.get(
            reverse("search_help"),
            {
                "query": "fa",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_search_help_page_name_is_not_search_details(self):
        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse("search_details"),
                {
                    "query": "fa",
                },
            )