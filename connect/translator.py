from modeltranslation.translator import TranslationOptions, register
from .models import Review, InfoContact, SendMessage


@register(Review)
class ReviewTranslationOption(TranslationOptions):
    fields = ['description']



