from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendMessageSerializer, InfoContactSerializer, ReviewSerializer
from rest_framework.permissions import AllowAny
from .models import InfoContact, Review
from drf_spectacular.utils import extend_schema


class SendMessageAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=SendMessageSerializer,
        responses={201: SendMessageSerializer},
        tags=['connect'],
        summary="send to message",
        description="tg botga habar yuborish"
    )
    def post(self, request):
        serializer = SendMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetInfoContactAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        contact_info = InfoContact.objects.all()

        serializer = InfoContactSerializer(contact_info, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetReviewAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)









