from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    FEMALE = 'F', _('Female')
    MALE = 'M', _('Male')
