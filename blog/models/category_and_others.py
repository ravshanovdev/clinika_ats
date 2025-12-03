from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"

    def __str__(self):
        return self.title


class Features(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        verbose_name = "Kichik ma'lumot"
        verbose_name_plural = "Kichik Ma'lumotlar"

    def __str__(self):
        return self.name


class ReliableService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    features = models.ManyToManyField(Features, blank=True)

    class Meta:
        verbose_name = "ishonchli xizmat"
        verbose_name_plural = "ishonchli xizmatlar"

    def __str__(self):
        return self.title


