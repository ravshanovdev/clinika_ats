from django.db import models


class Review(models.Model):
    username = models.CharField(max_length=150)
    description = models.TextField()
    grade = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'bemor qaydlari'
        verbose_name_plural = "bemor qaydlari"

    def __str__(self):
        return f"username: {self.username}"


class InfoContact(models.Model):
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    address = models.TextField()

    class Meta:
        verbose_name = "a'loqa ma'lumotlari"
        verbose_name_plural = "a'loqa ma'lumotlari"

    def __str__(self):
        return f"phone1: {self.phone1}"
