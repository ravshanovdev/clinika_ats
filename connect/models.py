from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    username = models.CharField(max_length=150, verbose_name=_('Username'))
    description = models.TextField(verbose_name=_('Description'))
    grade = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'bemor qaydlari'
        verbose_name_plural = "bemor qaydlari"

    def __str__(self):
        return f"username: {self.username}"


class InfoContact(models.Model):
    phone1 = models.CharField(max_length=20, verbose_name=_('Phone'))
    phone2 = models.CharField(max_length=20, blank=True, verbose_name=_('Phone'))
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    address = models.TextField(verbose_name=_('Address'))
    address2 = models.TextField(blank=True, verbose_name=_('Address'))

    class Meta:
        verbose_name = "a'loqa ma'lumotlari"
        verbose_name_plural = "a'loqa ma'lumotlari"

    def __str__(self):
        return f"phone1: {self.phone1}"


class SendMessage(models.Model):
    username = models.CharField(max_length=155, verbose_name=_('Username'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    email = models.EmailField()
    text = models.TextField(max_length=550, verbose_name=_('Text'))
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
