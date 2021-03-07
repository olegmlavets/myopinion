from django.core.mail import EmailMessage
import threading


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.email.send()


class Util:
    @staticmethod
    def send_email(data: dict) -> None:
        email = EmailMessage(**data)  # param "to" must be a tuple or list
        EmailThread(email).start()


def send(data: dict) -> bool:
    email = EmailMessage(**data)
    result = email.send()
    return result
