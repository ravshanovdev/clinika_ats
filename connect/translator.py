from modeltranslation.translator import TranslationOptions, register
from .models import Review, InfoContact, SendMessage


@register(Review)
class ReviewTranslationOption(TranslationOptions):
    fields = ['description']


@register(InfoContact)
class InfoContactTranslationOption(TranslationOptions):
    fields = ('address', 'address2')


