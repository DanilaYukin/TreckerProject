from datetime import datetime, time
from habit_tracker.services import send_telegram_message
from celery import shared_task
from .models import Habit


@shared_task
def remind_about_habit(habit_id):
    """Отправка напоминания о конкретной привычке"""

    try:
        habit = Habit.objects.get(id=habit_id)
        message = f"Время выполнить привычку: {habit.name}"
        user = habit.user
        send_telegram_message(chat_id=user.tg_chat_id, message=message)
        return f"Уведомление отправлено по привычке {habit_id}"
    except Habit.DoesNotExist:
        return f"Привычка {habit_id} не найдена"


@shared_task
def check_habit():
    now = datetime.now().time()
    current_time = time(now.hour, now.minute)

    habits_to_remind = Habit.objects.filter(
        time__hour=current_time.hour, time__minute=current_time.minute, is_active=True
    )

    for habit in habits_to_remind:
        remind_about_habit.delay(habit.id)
