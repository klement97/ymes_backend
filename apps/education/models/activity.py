from django.db import models
from django.db.models import Q, F
from django.utils.translation import gettext_lazy as _


class Activity(models.Model):
    start_time = models.TimeField(_('Start Time'))
    end_time = models.TimeField(_('End Time'))
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    message = models.CharField(_('Message'), max_length=250, blank=True)

    class Meta:
        db_table = 'activity'
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        ordering = ['start_time']
        constraints = [
            models.CheckConstraint(
                check=Q(start_time__lte=F('end_time')),
                name='correct_start_end_time'
            ),
        ]

    def __str__(self):
        return f'{self.start_time} - {self.end_time}: {self.name}'
