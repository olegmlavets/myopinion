from django.contrib.auth import get_user_model
from django.db import models
from authentication.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, related_name='profile', on_delete=models.CASCADE)

    SEXES = (
        ('Male', 1),
        ('Female', 2)
    )

    birthday = models.DateTimeField(null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    sex = models.IntegerField(choices=SEXES, blank=True, null=True, )
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} profile'
