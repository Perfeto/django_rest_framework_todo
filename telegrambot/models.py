from django.contrib.auth.models import User
from django.db import models


class TelegramProfile(models.Model):
    user = models.OneToOneField(
        to='auth.User',
        on_delete=models.CASCADE
    )
    external_id = models.PositiveIntegerField(
        verbose_name='ID user in tg'
    )
    name = models.TextField(
        verbose_name='User name'
    )


class Message(models.Model):
    message_owner = models.ForeignKey(
        to='telegrambot.TelegramProfile',
        related_name='messages',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Text'
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True
    )

    def __str__(self):
        return f'Message {self.pk,} from {self.message_owner}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
