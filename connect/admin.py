from django.contrib import admin
from .models import SendMessage, TgAdmin, InfoContact, Review

admin.site.register([SendMessage, TgAdmin, InfoContact, Review])
