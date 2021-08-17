from django.db import models
from django.utils.translation import gettext_lazy as _


class WeekMenu(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    is_active = models.BooleanField(_('Is Active'), default=False)
    organization = models.ForeignKey(
        verbose_name=_('Organization'),
        to='organization.Organization',
        on_delete=models.CASCADE,
        related_name='week_menu'
    )

    class Meta:
        verbose_name = 'Week Menu'
        verbose_name_plural = 'Week Menu'

    def __str__(self):
        return self.name
