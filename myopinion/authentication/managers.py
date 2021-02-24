from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str):

        if username is None:
            raise TypeError('User must have username')
        if email is None:
            raise TypeError('User must have email')
        if password is None:
            raise TypeError('User must have password')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)  # generate password-hash
        user.save()
        return user

    def create_superuser(self, username: str, email: str, password: str):
        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_stuff = True
        user.save()
        return user
