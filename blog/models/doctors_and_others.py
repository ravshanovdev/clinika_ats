from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Kasb'
        verbose_name_plural = 'Kasblar'

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Mutaxasislik'
        verbose_name_plural = 'Mutaxasisliklar'

    def __str__(self):
        return self.name


class AdditionalFeatures(models.Model):
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Qoshimcha Ma'lumotlar"
        verbose_name_plural = "Qoshimcha Ma'lumotlar"

    def __str__(self):
        return self.description


class Doctors(models.Model):
    name = models.CharField(max_length=150)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    specialty = models.ManyToManyField(Specialty, blank=True)
    experience = models.CharField(max_length=150)
    operations = models.CharField(max_length=150)
    certificates = models.ManyToManyField(AdditionalFeatures, blank=True)

    class Meta:
        verbose_name = 'Shifokor'
        verbose_name_plural = 'Shifokorlar'

    def __str__(self):
        return f"name: {self.name}, position: {self.position}"
