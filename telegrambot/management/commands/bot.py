from django.core.management import BaseCommand

from telegrambot.services.ServiceTelegramBot import ServiceTelegramBot


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        ServiceTelegramBot().start_bot()
