from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models.category_and_others import Category, Service
from .models.doctors_and_others import Doctors
from .models.statistic import Statistic
from .serializers import CategorySerializer, DoctorsSerializer, CommonStatisticSerializer, \
    ServiceSerializer, FirstPageStatisticSerializer
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema


class GetCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['category'],
        operation_summary='get all categories'
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





