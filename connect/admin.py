from django.contrib import admin
from .models import SendMessage, TgAdmin, InfoContact, Review
from modeltranslation.admin import TranslationAdmin

admin.site.register([InfoContact,SendMessage, TgAdmin, Review])

