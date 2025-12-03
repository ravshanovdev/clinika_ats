from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models.category_and_others import Category
from .models.doctors_and_others import Doctors
from .models.statistic import Statistic
from .serializers import CategorySerializer, DoctorsSerializer, StatisticSerializer
from rest_framework.permissions import AllowAny


class GetCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetDoctorsGenericAPIView(ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    permission_classes = [AllowAny]


class GetStatisticAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        statistics = Statistic.objects.all()

        serializer = StatisticSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



