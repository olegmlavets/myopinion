from myopinion.celery import app
from .models import User
from .utils import send, Util
from myopinion.settings import TIME_ZONE, EMAIL_HOST_USER
from datetime import datetime, timedelta
import pytz

SEND_MAIL_IN: int = 10  # in days


@app.task
def send_async_email(data: dict) -> None:
    send(data)


@app.task  # every 2 minutes check
def send_beat_email() -> None:
    actual = datetime.now(tz=pytz.timezone(TIME_ZONE))
    delta = timedelta(days=SEND_MAIL_IN)

    for user in User.objects.all():
        when_send = user.created_at + delta
        if when_send <= actual and not user.is_received_email:
            data = {
                'subject': 'Feedback',
                'body': 'Please leave feedback',
                'to': (user.email,),
                'from_email': EMAIL_HOST_USER,
            }

            send_async_email.delay(data=data)
            user.is_received_email = True
            user.save()
