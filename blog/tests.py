import pytest
from django.utils import translation
from .models.category_and_others import Category, ReliableService


@pytest.mark.django_db
def test_category():
    category = Category.objects.create(name="zo'r categoriya (uz)")
    category.name_en = 'best category (en)'
    category.name_ru = 'лучшая категория (ru)'
    category.save()

    translation.activate('ru')
    category.refresh_from_db()
    assert category.name == 'лучшая категория (ru)'

    translation.activate('en')
    category.refresh_from_db()
    assert category.name == 'best category (en)'

    translation.activate('uz')
    category.refresh_from_db()
    assert category.name == "zo'r categoriya (uz)"\



@pytest.mark.django_db
def test_reliable_service():
    service = ReliableService.objects.create(title="uzbekcha (uz)", description='eng zor tavsifi')
    service.title_en = 'english (en)'
    service.title_ru = 'Русский (ru)'
    service.description_en = 'best description (en)'
    service.description_ru = 'описание (ru)'
    service.save()

    translation.activate('ru')
    service.refresh_from_db()
    assert service.title == 'Русский (ru)'
    assert service.description == 'описание (ru)'

    translation.activate('en')
    service.refresh_from_db()
    assert service.title == 'english (en)'
    assert service.description == 'best description (en)'

    translation.activate('uz')
    service.refresh_from_db()
    assert service.title == "uzbekcha (uz)"
    assert service.description == 'eng zor tavsifi'



