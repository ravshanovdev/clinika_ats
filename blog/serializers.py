from rest_framework import serializers
from .models.category_and_others import Category, Service
from .models.doctors_and_others import Doctors, Specialty, AdditionalFeatures, Position
from .models.statistic import Statistic, AboutUs
from .models.location import Location


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ["id",
                  "title_uz", "title_ru", "title_en",
                  "description_uz", "description_ru", "description_en",
                  "working_graph_uz", "working_graph_ru", "working_graph_en",
                  "features_uz", "features_ru", "features_en"]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class AdditionalFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFeatures
        fields = ['id', 'description', 'description_uz', "description_ru", "description_en"]


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class DoctorsSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(many=True)
    certificates = AdditionalFeaturesSerializer(many=True)
    position = PositionSerializer()

    class Meta:
        model = Doctors
        fields = ['id', 'name', 'position', 'specialty', 'experience',
                  'operations', 'certificates', 'image']


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
