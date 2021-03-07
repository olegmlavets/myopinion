import os
from celery import Celery

# We will set the celery-settings in django-settings and will give it to Celery via ENV VAR
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myopinion.settings')

app = Celery('myopinion')

# all celery settings must have CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto search for tasks - ON
app.autodiscover_tasks()
