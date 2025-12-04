from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models.category_and_others import Category, Service
from .models.doctors_and_others import Doctors
from .models.statistic import Statistic
from .models.location import Location
from .serializers import CategorySerializer, DoctorsSerializer, CommonStatisticSerializer, \
    ServiceSerializer, FirstPageStatisticSerializer, LocationSerializer
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema


class GetCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        description="get category",
    )
    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetDoctorsGenericAPIView(ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    permission_classes = [AllowAny]


class GetCommonPageStatisticAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        statistics = Statistic.objects.all()

        serializer = CommonStatisticSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetFirstPageStatisticAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        statistics = Statistic.objects.all()

        serializer = FirstPageStatisticSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetServiceAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        service = Service.objects.all()

        serializer = ServiceSerializer(service, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetLocationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



