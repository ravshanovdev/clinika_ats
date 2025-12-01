from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Features(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class ReliableService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    features = models.ManyToManyField(Features, blank=True)

    def __str__(self):
        return self.title


