from django.urls import path
from .views import GetCategoryAPIView, GetDoctorsGenericAPIView, GetCommonPageStatisticAPIView,\
    GetServiceAPIView, GetFirstPageStatisticAPIView, GetLocationAPIView


urlpatterns = [
    path('get_categories/', GetCategoryAPIView.as_view(), ),
    path('get_doctors/', GetDoctorsGenericAPIView.as_view(), ),
    path('get-common-statistic/', GetCommonPageStatisticAPIView.as_view(), ),
    path('get-services/', GetServiceAPIView.as_view(), ),
    path('get-first-page-statistic/', GetFirstPageStatisticAPIView.as_view(), ),
    path('get-location/', GetLocationAPIView.as_view(), ),



]



