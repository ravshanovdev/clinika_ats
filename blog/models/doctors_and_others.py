from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class AdditionalFeatures(models.Model):
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description


class Doctors(models.Model):
    name = models.CharField(max_length=150)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    experience = models.CharField(max_length=150)
    operations = models.CharField(max_length=150)
    certificates = models.ManyToManyField(AdditionalFeatures, blank=True)

    def __str__(self):
        return f"name: {self.name}, position: {self.position}"
