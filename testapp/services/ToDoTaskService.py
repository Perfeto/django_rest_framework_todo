from telegrambot.models import TelegramProfile
from telegrambot.services.ServiceTelegramBot import ServiceTelegramBot
from testapp.models import ToDoTask
from testapp.serializers import ToDoTaskSerializer


def get_todo_tasks_for_user(owner_id: int):
    to_do_items_list = ToDoTask.objects.filter(owner_id=owner_id)
    return to_do_items_list


def on_task_created_telegram_notify(task_id: int):
    saved_to_do_task = \
        ToDoTask.objects.filter(
            id=task_id
        ).first()

    telegram_user = \
        TelegramProfile.objects.filter(
            user_id=saved_to_do_task.owner_id
        ).first()

    ServiceTelegramBot().send_text_to_telegram(
        saved_to_do_task.__str__(),
        telegram_user.external_id
    )
