from rest_framework import serializers
from .models import SendMessage, InfoContact, Review


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessage
        fields = ['id', 'username', 'phone', 'email', 'text']


class InfoContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoContact
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
