from django.core.management.base import BaseCommand
from apps.users.init_db import run_all_creations

class Command(BaseCommand):
    help = "Crea todas las tablas necesarias en la base de datos."

    def handle(self, *args, **kwargs):
        try:
            run_all_creations()
            self.stdout.write(self.style.SUCCESS("Todas las tablas fueron creadas correctamente."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))