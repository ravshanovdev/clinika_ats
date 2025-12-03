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

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return f"expertlar soni: {self.experts} ta"


class AboutUs(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=155)
    description = models.TextField()
    working_graph = models.JSONField(default=dict)
    features = models.TextField(blank=True)

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"

    def __str__(self):
        return self.title








