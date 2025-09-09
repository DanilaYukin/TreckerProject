from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "action")
