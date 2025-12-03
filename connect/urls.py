from django.urls import path
from .views import SendMessageAPIView, GetInfoContactAPIView, GetReviewAPIView


urlpatterns = [
    path('send-message/', SendMessageAPIView.as_view(), ),
    path('contact-info/', GetInfoContactAPIView.as_view(), ),
    path('get-reviews/', GetReviewAPIView.as_view(), ),

]
