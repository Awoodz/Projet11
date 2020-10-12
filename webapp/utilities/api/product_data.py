from dictor import dictor


class Product_data:
    """Gathers product data"""

    def __init__(self, product_data):
        self.datas = product_data

    @property
    def product_id(self):
        return dictor(self.datas, "code")

    @property
    def img(self):
        return dictor(self.datas, "product.selected_images.front.display.fr")

    @property
    def url(self):
        return "https://fr.openfoodfacts.org/produit/" + dictor(self.datas, "code")

    @property
    def name(self):
        return dictor(self.datas, "product.product_name_fr")

    @property
    def energy_kj(self):
        return dictor(self.datas, "product.nutriments.energy_100g")

    @property
    def energy_kcal(self):
        return dictor(self.datas, "product.nutriments.energy-kcal_100g")

    @property
    def carbohydrates(self):
        return dictor(self.datas, "product.nutriments.carbohydrates_100g")

    @property
    def sugar(self):
        return dictor(self.datas, "product.nutriments.sugars_100g")

    @property
    def lipids(self):
        return dictor(self.datas, "product.nutriments.fat_100g")

    @property
    def fat(self):
        return dictor(self.datas, "product.nutriments.saturated-fat_100g")

    @property
    def salt(self):
        return dictor(self.datas, "product.nutriments.salt_100g")

    @property
    def sodium(self):
        return dictor(self.datas, "product.nutriments.sodium_100g")

    @property
    def protein(self):
        return dictor(self.datas, "product.nutriments.proteins_100g")

    @property
    def nutriscore(self):
        return dictor(self.datas, "product.nutriscore_grade")
