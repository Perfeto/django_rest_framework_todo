from rest_framework import serializers

from telegrambot.models import TelegramProfile


class TelegramProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramProfile
        fields = ['external_id']
