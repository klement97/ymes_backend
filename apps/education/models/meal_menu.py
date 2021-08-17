from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.choices import Meal, Day


class MealMenu(models.Model):
    meal = models.IntegerField(_('Meal'), choices=Meal.choices)
    day = models.IntegerField(_('Day'), choices=Day.choices)
    food = models.CharField(_('Food'), max_length=100)
    week = models.ForeignKey(
        verbose_name=_('Week'),
        to='education.WeekMenu',
        on_delete=models.CASCADE,
        related_name='meal_menu'
    )

    class Meta:
        verbose_name = 'Meal Menu'
        verbose_name_plural = 'Meal Menu'
        ordering = ['meal']

    def __str__(self):
        return f'{self.meal} {self.day} {self.week}'
