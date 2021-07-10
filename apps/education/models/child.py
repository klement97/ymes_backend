from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.utils import Gender


class Child(models.Model):
    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    mother_name = models.CharField(_('Mother name'), max_length=50)
    father_name = models.CharField(_('Father name'), max_length=50)
    birthplace = models.CharField(_('Birthplace'), max_length=100)
    birthdate = models.DateField(_('Birthdate'))
    gender = models.CharField(max_length=1, choices=Gender.choices)

    parents = models.ManyToManyField(
        verbose_name=_('Parents'),
        to=settings.AUTH_USER_MODEL,
        related_name='children',
    )
    group = models.ForeignKey(
        verbose_name=_('Group'),
        to=Group,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = 'Child'
        verbose_name_plural = 'Children'
        db_table = 'child'

    def __str__(self) -> str:
        return f'{self.first_name} {self.father_name} {self.last_name}'
