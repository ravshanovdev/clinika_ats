from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Name')
    address = models.CharField(max_length=255, blank=True, verbose_name='Address')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

