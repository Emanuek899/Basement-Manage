import os
from celery import Celery

os.environ.setdefault('DJANGO.SETTINGS.MODULE', 'settins.settings')
app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
