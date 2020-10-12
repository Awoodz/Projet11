from django.test import TestCase
from django.urls import reverse
from webapp.models import Product, Category


class AutoCompletePageTestCase(TestCase):
    def test_if_autocomplete_page_display_json_products_list(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )

        product_id = str(Product.objects.get(product_name="Fake product").id)
        product_name = Product.objects.get(product_name="Fake product").product_name

        response = self.client.get(reverse("autocomplete"),)
        self.assertEqual(
            response.json(),
            {
                "results": [
                    {
                        "id": product_id,
                        "text": product_name,
                        "selected_text": product_name,
                    }
                ],
                "pagination": {"more": False},
            },
        )
