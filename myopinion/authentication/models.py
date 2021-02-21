from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, password: str = None):

        if username is None:
            raise TypeError('Users must have username')
        if email is None:
            raise TypeError('Users must have email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)  # if None, will  be generated random password
        user.save()
        return user

    def create_superuser(self, username: str, email: str, password: str):
        user = self.model(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_stuff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def tokens(self) -> dict:
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh),
                'access': str(refresh.access_token)}

    def __str__(self):
        return self.email
