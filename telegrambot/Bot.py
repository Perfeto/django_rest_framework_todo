from telegram import Bot, Update
from telegram.ext import CallbackContext, MessageHandler, Filters, Updater, CommandHandler
from telegram.utils.request import Request

from django_movie import settings
from telegrambot.models import TelegramProfile
from testapp.models import ToDoTask


class TelegramBot:
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
            cls.instance = super(TelegramBot, cls).__new__(cls)
        return cls.instance

    def start_bot(self):
        command_handler_get_to_do_list = CommandHandler('get_todo_list', callback=get_list_todos)
        self.updater.dispatcher.add_handler(command_handler_get_to_do_list)

        command_handler_get_to_do_list2 = MessageHandler(Filters.text, do_echo)
        self.updater.dispatcher.add_handler(command_handler_get_to_do_list2)

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
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    reply_text = "Your ID = {}\n\n{}".format(chat_id, text)
    print(f'{15 * "="} START {15 * "="}\n{reply_text}\n{15 * "="}  END  {15 * "="}')
    update.message.reply_text(
        text=reply_text
    )


@log_errors
def get_list_todos(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    telegram_profile = TelegramProfile.objects.filter(external_id=chat_id).first()
    to_do_tasks = ToDoTask.objects.filter(owner_id=telegram_profile.user_id)

    for todo_item in to_do_tasks:
        update.message.reply_text(text=todo_item.__str__())
