from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))

    class Meta:
        verbose_name = 'Kasb'
        verbose_name_plural = 'Kasblar'

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))

    class Meta:
        verbose_name = 'Mutaxasislik'
        verbose_name_plural = 'Mutaxasisliklar'

    def __str__(self):
        return self.name


class AdditionalFeatures(models.Model):
    description = models.TextField(max_length=500, verbose_name=_('Description'))

    class Meta:
        verbose_name = "Qoshimcha Ma'lumotlar"
        verbose_name_plural = "Qoshimcha Ma'lumotlar"

    def __str__(self):
        return self.description


class Doctors(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    image = models.ImageField(upload_to='images/', blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    specialty = models.ManyToManyField(Specialty, blank=True)
    experience = models.IntegerField(default=0)
    operations = models.CharField(max_length=150, verbose_name=_('Operations'))
    certificates = models.ManyToManyField(AdditionalFeatures, blank=True)

    class Meta:
        verbose_name = 'Shifokor'
        verbose_name_plural = 'Shifokorlar'

    def __str__(self):
        return f"name: {self.name}, position: {self.position}"
