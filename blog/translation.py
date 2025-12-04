from modeltranslation.translator import register, TranslationOptions

from .models.doctors_and_others import Doctors, Position, Specialty, \
    AdditionalFeatures

from .models.statistic import AboutUs
from .models.category_and_others import Category, Service, Features, ReliableService


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ['name']


@register(ReliableService)
class ReliableService(TranslationOptions):
    fields = ['title', 'description', 'features']


@register(Service)
class ServiceTranslationOption(TranslationOptions):
    fields = ['title', 'description']


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['name']


@register(AboutUs)
class AboutUsTranslationOption(TranslationOptions):
    fields = ['title', 'description', 'working_graph', 'features']


@register(AdditionalFeatures)
class AdditionalFeatures(TranslationOptions):
    fields = ['description']


@register(Specialty)
class SpecialityTranslationOption(TranslationOptions):
    fields = ['name']


@register(Position)
class PositionTranslationOption(TranslationOptions):
    fields = ['name']


@register(Doctors)
class DoctorsTranslationOption(TranslationOptions):
    fields = ['position', 'specialty', 'certificates']




