from django.apps import AppConfig
from . import models

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.API'

    def ready(self):
        models.create_token_table()