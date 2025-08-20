from rest_framework import serializers
from habit_tracker.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user",)

    def validate(self, data):
        """Добавляем валидацию из модели"""

        if data.get("is_pleasant") and (data.get("link_habit") or data.get("reward")):
            raise serializers.ValidationError(
                "Приятная привычка не может иметь связанной привычки или вознаграждения!"
            )
        return data
