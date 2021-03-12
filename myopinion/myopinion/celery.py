import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
# We will set the celery-settings in django-settings and will give it to Celery via ENV VAR
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myopinion.settings')

app = Celery('myopinion')

# all celery settings must have CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto search for tasks - ON
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-feedback-email-in-10-days': {
        'task': 'authentication.tasks.send_beat_email',
        'schedule': crontab(hour=f'*/{settings.CHECK_SEND_INTERVAL}')  # * times every day
    }
}
