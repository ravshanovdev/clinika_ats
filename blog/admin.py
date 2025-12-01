from django.contrib import admin
from .models.category_and_others import Category, Service, Features, ReliableService
from .models.doctors_and_others import Position, Specialty, AdditionalFeatures, Doctors
from .models.statistic import Statistic, AboutUs

admin.site.register([Category, Service, Features, ReliableService, Position, Specialty, AdditionalFeatures, Doctors, Statistic, AboutUs])
