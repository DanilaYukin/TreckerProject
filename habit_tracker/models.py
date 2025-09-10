from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
from django.utils import timezone


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место",
        help_text="Место в котором необходимо выполнять привычку",
    )
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=250, verbose_name="Действие")
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    link_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        related_name="main_habits",
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        verbose_name="Периодичность (в днях)",
    )
    reward = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Вознаграждение"
    )
    duration = models.PositiveIntegerField(
        validators=[MaxValueValidator(120)],
        verbose_name="Время на выполнение (в секундах)",
    )
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")
    last_completed = models.DateField(
        null=True, blank=True, verbose_name="Дата последнего выполнения"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Владелец",
        related_name="habit_owner",
    )

    def __str__(self):
        return f"{self.action} в {self.time} ({self.place})"

    def clean(self):
        """Валидация перед сохранением"""

        if self.is_pleasant and (self.reward or self.link_habit):
            raise ValidationError(
                "Приятная привычка не может иметь вознаграждения или связанной привычки!"
            )

        if not self.is_pleasant and self.link_habit and self.reward:
            raise ValidationError(
                "У полезной привычки может быть только связанная привычка ИЛИ вознаграждение!"
            )

        if self.link_habit and not self.link_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной!")

        if self.periodicity > 7:
            raise ValidationError("Привычку нельзя выполнять реже, чем раз в 7 дней!")

    def save(self, *args, **kwargs):
        """Дополнительная проверка перед сохранением"""
        self.clean()  # Вызов валидации
        super().save(*args, **kwargs)

    def check_completion_frequency(self):
        """Проверяет, выполнена ли привычка хотя бы раз за последние 7 дней"""

        if self.last_completed:
            days_passed = (timezone.now().date() - self.last_completed).days
            if days_passed > 7:
                return False
        return True

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
