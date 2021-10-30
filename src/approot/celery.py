import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'approot.settings')

app = Celery('approot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()