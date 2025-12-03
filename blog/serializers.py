from rest_framework import serializers
from .models.category_and_others import Category, Service
from .models.doctors_and_others import Doctors
from .models.statistic import Statistic
from .models.location import Location


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'name', 'position', 'specialty', 'experience', 'operations', 'certificates']


class CommonStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['id', 'rooms', 'experts', 'certificates', 'wheelchair']


class FirstPageStatisticSerializer(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField()

    class Meta:
        model = Statistic
        fields = ['id', 'happy_patients', 'experts', 'awards', 'experience']

    def get_experience(self, obj):
        experiences = Doctors.objects.all().values_list('experience', flat=True)

        numbers = []

        for exp in experiences:
            try:
                numbers.append(float(exp))
            except:
                pass

        if not numbers:
            return 5

        return int(sum(numbers) / len(numbers))


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'image']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'latitude', 'longitude']
