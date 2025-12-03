from django.urls import path
from .views import GetCategoryAPIView, GetDoctorsGenericAPIView, GetStatisticAPIView


urlpatterns = [
    path('get_categories/', GetCategoryAPIView.as_view(), ),
    path('get_doctors/', GetDoctorsGenericAPIView.as_view(), ),
    path('get-statistic/', GetStatisticAPIView.as_view(), ),



]



