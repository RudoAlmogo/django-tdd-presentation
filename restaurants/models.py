from django.db import models
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    id: int
    name = models.CharField(_('name'), max_length=255)
    address = models.CharField(_('address'), max_length=255)
    opening_time = models.TimeField(_('opening_time'))
    closing_time = models.TimeField(_('closing_time'))
    active = models.BooleanField(_('active'))

    def __str__(self) -> str:
        return self.name
