from django.core.management import BaseCommand

from telegrambot.Bot import TelegramBot


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        TelegramBot().start_bot()
