# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from telegrambot.Bot import TelegramBot
from telegrambot.models import TelegramProfile
from telegrambot.serializers import TelegramProfileCreateSerializer


class TelegramProfileCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TelegramProfileCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        telegram_user = \
            TelegramProfile.objects.filter(user_id=self.request.user.pk).first()

        TelegramBot().send_text_to_telegram("Hi, i am your todo bot!", telegram_user.external_id)
