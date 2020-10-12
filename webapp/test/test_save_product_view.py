from django.test import TestCase
from django.urls import reverse
from webapp.models import Product, Category
from userapp.models import CustomUser


class SaveProductPageTestCase(TestCase):
    def test_if_save_product_page_works(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        product_id = Product.objects.get(product_name="Fake product").id

        user_login = self.client.force_login(user)

        self.client.get(reverse("save_product"), {"product_token": product_id,})
        self.assertEqual(
            fake_prod.user_product.filter(username="Fakeuser").exists(), True
        )
