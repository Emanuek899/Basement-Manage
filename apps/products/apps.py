from django.apps import AppConfig
from . import models as m

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'

    def ready(self):
        m.create_products_table()
        m.create_categories_table()
        m.create_product_categories_table()