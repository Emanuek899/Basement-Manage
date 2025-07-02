from django.apps import AppConfig
from .models import create_users_table


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
