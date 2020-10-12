from django.core.management.base import BaseCommand
from webapp.utilities.sql.sql_insert import Sql_insert


class Command(BaseCommand):
    def handle(self, *args, **options):
        Sql_insert.product_updater()
