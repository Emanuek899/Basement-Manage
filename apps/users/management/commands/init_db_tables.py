from django.core.management.base import BaseCommand
from apps.users.init_db import run_all_creations

class Command(BaseCommand):
    help = "Crea todas las tablas necesarias en la base de datos."

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando creación de tablas...')
        try:
            run_all_creations(self.stdout)
            self.stdout.write(self.style.SUCCESS("Todas las tablas fueron creadas correctamente."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
            raise  # Muy importante para que el error no se oculte y Railway lo detecte
