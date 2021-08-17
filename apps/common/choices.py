from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    FEMALE = 'F', _('Female')
    MALE = 'M', _('Male')


class Meal(models.IntegerChoices):
    BREAKFAST = 1, _('Breakfast')
    BRUNCH = 2, _('Brunch')
    LUNCH = 3, _('Lunch')
    TEA = 4, _('Tea')


class Day(models.IntegerChoices):
    MONDAY = 0, _('Monday')
    TUESDAY = 1, _('Tuesday')
    WEDNESDAY = 2, _('Wednesday')
    THURSDAY = 3, _('Thursday')
    FRIDAY = 4, _('Friday')
    SATURDAY = 5, _('Saturday')
    SUNDAY = 6, _('Sunday')
