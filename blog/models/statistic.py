from django.db import models
from .doctors_and_others import Doctors
from .category_and_others import Features


def get_doctors_count():
    return Doctors.objects.count()


class Statistic(models.Model):
    experts = models.IntegerField(default=get_doctors_count)
    rooms = models.IntegerField(default=0, blank=True)
    certificates = models.IntegerField(default=0, blank=True)
    num_strollers = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.experts


class AboutUs(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    features = models.ManyToManyField(Features, blank=True)

    def __str__(self):
        return self.title








