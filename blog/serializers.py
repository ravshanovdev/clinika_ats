from rest_framework import serializers
from .models.category_and_others import Category
from .models.doctors_and_others import Doctors
from .models.statistic import Statistic


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'name', 'position', 'specialty', 'experience', 'operations', 'certificates']


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['id', 'rooms', 'experts', 'certificates', 'num_strollers']
