from django.test import TestCase
from django.urls import reverse
from webapp.models import Product, Category


class AjaxSearchPageTestCase(TestCase):
    def test_search_page_filters_nutriscore(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod_e = Product.objects.create(
            product_name="Fake product e",
            product_url="http://fake_product_e.com",
            product_img="http://fake_product_e.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        fake_prod_d = Product.objects.create(
            product_name="Fake product d",
            product_url="http://fake_product_d.com",
            product_img="http://fake_product_d.com/fakeprod.png",
            product_nutriscore="d",
            product_category_id=fake_cat,
        )

        product_id = Product.objects.get(product_name="Fake product e").id
        nutrichar = "d"

        response = self.client.get(reverse("ajax_search"), {"nutrichar": nutrichar, "search_prod": product_id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fake product d")