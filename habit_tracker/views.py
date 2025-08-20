from rest_framework import generics
from users.permissions import IsOwner
from .models import Habit
from .serializers import HabitSerializer
from .paginators import HabitPaginator


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUserListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        user_habits = Habit.objects.filter(user=user)
        return user_habits


class HabitIsPublicListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.filter(is_public=True)


class HabitRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateApiView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyApiView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
