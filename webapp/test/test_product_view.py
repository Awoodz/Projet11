from django.test import TestCase
from django.urls import reverse
from webapp.models import Product, Nutriments, Category


class ProductPageTestCase(TestCase):
    def test_product_page_returns_200(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        fake_nutri = Nutriments.objects.create(
            nutriments_product_id=fake_prod,
            nutriments_kj="0",
            nutriments_kcal="0",
            nutriments_lipids="0",
            nutriments_fat="0",
            nutriments_carbohydrates="0",
            nutriments_sugar="0",
            nutriments_protein="0",
            nutriments_salt="0",
            nutriments_sodium="0",
        )
        product_id = Product.objects.get(product_name="Fake product").id
        response = self.client.get(reverse("product", args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    def test_product_page_returns_404(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        fake_nutri = Nutriments.objects.create(
            nutriments_product_id=fake_prod,
            nutriments_kj="0",
            nutriments_kcal="0",
            nutriments_lipids="0",
            nutriments_fat="0",
            nutriments_carbohydrates="0",
            nutriments_sugar="0",
            nutriments_protein="0",
            nutriments_salt="0",
            nutriments_sodium="0",
        )
        product_id = Product.objects.get(product_name="Fake product").id + 1
        response = self.client.get(reverse("product", args=(product_id,)))
        self.assertEqual(response.status_code, 404)
