import telegram
from telegram import Bot, Update
from telegram.ext import CallbackContext, Updater, CommandHandler
from telegram.utils.request import Request

from django_movie import settings
from telegrambot.models import TelegramProfile
from testapp.models import ToDoTask


class ServiceTelegramBot:
    # 1 -- right connection
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0
    )
    bot = Bot(
        request=request,
        token=settings.TELEGRAM_BOT_API_KEY
    )
    # 2 -- handlers
    updater = Updater(
        bot=bot,
        use_context=True
    )

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ServiceTelegramBot, cls).__new__(cls)
        return cls.instance

    def start_bot(self):
        command_handler_get_to_do_list = CommandHandler('get_todo_list', callback=get_list_todos)
        self.updater.dispatcher.add_handler(command_handler_get_to_do_list)

        command_handler_get_chat_id = CommandHandler('start', callback=return_chat_id)
        self.updater.dispatcher.add_handler(command_handler_get_chat_id)

        # 3 -- run endless loop
        self.updater.start_polling()
        self.updater.idle()

    def send_text_to_telegram(self, text: str, chat_id: int):
        self.bot.send_message(chat_id=chat_id, text=text)


# Decorators
def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Error: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def return_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    reply_text = "\nYour chat_id is:\n<b>{}</b>\n".format(chat_id)
    update.message.reply_text(
        text=reply_text,
        parse_mode=telegram.ParseMode.HTML
    )


@log_errors
def get_list_todos(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    telegram_profile = TelegramProfile.objects.filter(external_id=chat_id).first()
    to_do_tasks = ToDoTask.objects.filter(owner_id=telegram_profile.user_id)

    for todo_item in to_do_tasks:
        update.message.reply_text(text=todo_item.__str__())
