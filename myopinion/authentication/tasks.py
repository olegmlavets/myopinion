from myopinion.celery import app

from .utils import send, Util


@app.task
def send_async_email(data: dict):
    send(data)


