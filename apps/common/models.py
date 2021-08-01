from django.db import models


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Track(models.Model):
    created_at = models.DateTimeField('Date created', auto_now_add=True)
    updated_at = models.DateTimeField('Date last updated', auto_now=True)

    class Meta:
        abstract = True
