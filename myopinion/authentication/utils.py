from django.core.mail import EmailMessage
import threading


def send(data: dict) -> bool:
    email = EmailMessage(**data)
    result = email.send()
    return result
