from django.contrib import admin

# Register your models here.
from telegrambot.models import Message, TelegramProfile


@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name', 'user')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_owner', 'text', 'created_at',)
