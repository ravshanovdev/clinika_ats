from django.contrib import admin
from .models import SendMessage, TgAdmin

admin.site.register([SendMessage, TgAdmin])
