from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.authentication.managers import UserManager


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    username = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
