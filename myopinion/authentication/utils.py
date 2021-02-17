from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data: dict) -> bool:
        email = EmailMessage(**data)  # param "to" must be a tuple or list

        return email.send()
