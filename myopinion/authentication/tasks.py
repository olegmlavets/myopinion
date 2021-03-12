from myopinion.celery import app
from .models import User
from .utils import send
from django.conf import settings
from datetime import timedelta
from django.utils import timezone


@app.task
def send_async_email(data: dict) -> None:
    send(data)


@app.task  # every 2 minutes check
def send_beat_email() -> None:
    actual = timezone.now()
    delta = timedelta(days=settings.SEND_MAIL_FEEDBACK_IN)

    for user in User.objects.all():
        when_send = user.created_at + delta
        if when_send <= actual and not user.is_received_email:
            data = {
                'subject': 'Feedback',
                'body': 'Please leave feedback',
                'to': (user.email,),
                'from_email': settings.EMAIL_HOST_USER,
            }

            send_async_email.delay(data=data)
            user.is_received_email = True
            user.save()
