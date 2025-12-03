from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

