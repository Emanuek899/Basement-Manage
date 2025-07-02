from django.apps import AppConfig
from . import models as m


class ProvidersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.providers"

    def ready(self):
        m.create_providers_table()
        m.create_product_providers_table()
