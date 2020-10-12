import logging

from django.db import DatabaseError, transaction

from unidecode import unidecode

import webapp.utilities.data as dt
from webapp.models import Category, Nutriments, Product
from webapp.utilities.api.product_data import Product_data
from webapp.utilities.api.requester import Requester


class Sql_insert:
    """Makes insertions in database"""

    def product_inserter():
        """Makes category and product insertion in database"""
        # setting the logger
        logger = logging.getLogger(__name__)
        # emptying the database
        Category.objects.all().delete()
        Product.objects.all().delete()
        Nutriments.objects.all().delete()

        i = 0
        # for each category in category list
        for elem in dt.CAT_LIST:
            # Replace some characters with others, so we can use it in API
            elem = elem.replace(" ", "-")
            # create a category in database
            category = Category(category_name=unidecode(elem))
            # save if ok
            try:
                with transaction.atomic():
                    category.save()
            # report error if not ok
            except DatabaseError as cat_error:
                logger.error(cat_error)
                pass

            # get id list using Requester class
            id_list = Requester(elem).product_id_list

            # for each product id in id list
            for product_id in id_list:
                # gather product data with Requester class
                product_data = Product_data(
                    Requester.product_data_requester(product_id)
                )
                # create a product in database
                product = Product(
                    product_name=product_data.name,
                    product_url=product_data.url,
                    product_img=product_data.img,
                    product_nutriscore=product_data.nutriscore,
                    product_category_id=category,
                )
                # create nutriments data affiliated to product
                nutriments = Nutriments(
                    nutriments_product_id=product,
                    nutriments_kj=product_data.energy_kj,
                    nutriments_kcal=product_data.energy_kcal,
                    nutriments_lipids=product_data.lipids,
                    nutriments_fat=product_data.fat,
                    nutriments_carbohydrates=product_data.carbohydrates,
                    nutriments_sugar=product_data.sugar,
                    nutriments_protein=product_data.protein,
                    nutriments_salt=product_data.salt,
                    nutriments_sodium=product_data.sodium,
                )
                # save if ok
                try:
                    with transaction.atomic():
                        product.save()
                        nutriments.save()
                        i += 1
                        print(str(i) + " produit(s) ajouté(s)")
                # report error if not ok
                except DatabaseError as prod_error:
                    logger.error(prod_error)
                    pass

    def user_saved_product_inserter(product, user):
        """Save a user product"""
        # setting the logger
        logger = logging.getLogger(__name__)
        # create link between product and user
        product.user_product.add(user)
        # save if ok
        try:
            with transaction.atomic():
                product.save()
        # report error if not ok
        except DatabaseError as save_error:
            logger.error(save_error)
            pass

    def product_updater():
        """Makes new product insertion in database"""
        # setting the logger
        logger = logging.getLogger(__name__)
        # emptying the database

        i = 0
        # for each category in category list
        for elem in dt.CAT_LIST:
            # Replace some characters with others, so we can use it in API
            elem = elem.replace(" ", "-")
            elem = unidecode(elem)
            # get id list using Requester class
            category = Category.objects.get(category_name=elem)
            id_list = Requester(elem).product_id_list
            # for each product id in id list
            for product_id in id_list:
                # gather product data with Requester class
                product_data = Product_data(
                    Requester.product_data_requester(product_id)
                )
                # create a product in database
                product = Product(
                    product_name=product_data.name,
                    product_url=product_data.url,
                    product_img=product_data.img,
                    product_nutriscore=product_data.nutriscore,
                    product_category_id=category,
                )
                # create nutriments data affiliated to product
                nutriments = Nutriments(
                    nutriments_product_id=product,
                    nutriments_kj=product_data.energy_kj,
                    nutriments_kcal=product_data.energy_kcal,
                    nutriments_lipids=product_data.lipids,
                    nutriments_fat=product_data.fat,
                    nutriments_carbohydrates=product_data.carbohydrates,
                    nutriments_sugar=product_data.sugar,
                    nutriments_protein=product_data.protein,
                    nutriments_salt=product_data.salt,
                    nutriments_sodium=product_data.sodium,
                )
                # save if ok
                try:
                    with transaction.atomic():
                        product.save()
                        nutriments.save()
                        i += 1
                        print(str(i) + " produit(s) ajouté(s)")
                # report error if not ok
                except DatabaseError as prod_error:
                    logger.error(prod_error)
                    pass
