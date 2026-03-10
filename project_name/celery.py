import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
os.environ.setdefault('CELERY_CONFIG_MODULE', '{{ project_name }}.celeryconfig_dev')
app = Celery("{{ project_name }}")
app.config_from_object('{{ project_name }}.celeryconfig_dev')
app.autodiscover_tasks()
