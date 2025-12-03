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
    address2 = models.TextField(blank=True)

    class Meta:
        verbose_name = "a'loqa ma'lumotlari"
        verbose_name_plural = "a'loqa ma'lumotlari"

    def __str__(self):
        return f"phone1: {self.phone1}"


class SendMessage(models.Model):
    username = models.CharField(max_length=155)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField(max_length=550)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'habar'
        verbose_name_plural = "habarlar"

    def __str__(self):
        return self.username


class TgAdmin(models.Model):
    username = models.CharField(max_length=150)
    chat_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'telegram admin'
        verbose_name_plural = 'telegram_adminlari'

    def __str__(self):
        return f"{self.username} -- {self.chat_id}"
