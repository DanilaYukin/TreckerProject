from django.urls import path

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import (
    HabitCreateApiView,
    HabitUpdateApiView,
    HabitDestroyApiView,
    HabitRetrieveApiView,
    HabitUserListApiView,
    HabitIsPublicListApiView,
)

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("habits_user/", HabitUserListApiView.as_view(), name="habits_user_list"),
    path("habits_public/", HabitIsPublicListApiView.as_view(), name="habits_public_list"),
    path("habit/<int:pk>/", HabitRetrieveApiView.as_view(), name="habit_get"),
    path("habit/update/<int:pk>/", HabitUpdateApiView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habit_delete"),
]
