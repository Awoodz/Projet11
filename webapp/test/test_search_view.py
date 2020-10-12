from django.test import TestCase
from django.urls import reverse
from webapp.models import Product, Category


class SearchPageTestCase(TestCase):
    def test_search_page_if_autocomplete_search_form_is_used(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )

        product_id = Product.objects.get(product_name="Fake product").id

        response = self.client.get(reverse("search"), {"product_search": product_id,})
        self.assertEqual(response.status_code, 200)

    def test_search_page_if_classic_search_form_is_used_with_complete_name(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )

        response = self.client.get(
            reverse("search"), {"product_search": "Fake product",}
        )
        self.assertEqual(response.status_code, 200)

    def test_search_page_if_classic_search_form_is_used_with_incomplete_name(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )

        response = self.client.get(reverse("search"), {"product_search": "fa",})
        self.assertEqual(response.status_code, 302)
