from django.core.management import BaseCommand

from telegrambot.services.ServiceTelegramBot import ServiceTelegramBot


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        TelegramBot().start_bot()
