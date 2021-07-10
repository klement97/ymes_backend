from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.authentication.managers import UserManager
from apps.common.utils import Gender


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, db_index=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    residence = models.CharField(max_length=100, null=True)
    emergency_number = models.CharField(max_length=20, null=True)
    username = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
