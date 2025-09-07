from rest_framework import status
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@lms.ru")
        self.client.force_authenticate(self.user)
        self.habit = Habit.objects.create(
            user=self.user, place='Place Test', time='00:00', action='Action Test', is_pleasant=True, periodicity=1,
            duration=60, is_public=True, last_completed="2023-05-05", owner=self.user
        )

    def test_create_habit(self):
        self.data = {"user": self.user.id, "place": "Place Test", "time": "00:00", "action": "Action Test",
                     "is_pleasant": True, "periodicity": 1, "duration": 60, "is_public": True,
                     "last_completed": "2023-05-05"}

        response = self.client.post("/habit/create/", data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Habit.objects.all().exists())

    def test_list_habits_user(self):
        """Тестирование списка задач пользователя"""
        habit = Habit.objects.create(
            user=self.user, place='Place Test', time='00:00', action='Action Test', is_pleasant=True, periodicity=1,
            duration=60, is_public=True, last_completed="2023-05-05", owner=self.user
        )

        response = self.client.get("/habits_user/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_habits_is_public(self):
        """Тестирование списка публичных задач"""
        habit = Habit.objects.create(
            user=self.user, place='Place Test', time='00:00', action='Action Test', is_pleasant=True, periodicity=1,
            duration=60, is_public=True, last_completed="2023-05-05", owner=self.user
        )

        response = self.client.get("/habits_public/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """Тестирование обновления задачи"""
        habit = Habit.objects.create(
            user=self.user, place='Place Test', time='00:00', action='Action Test', is_pleasant=True, periodicity=1,
            duration=60, is_public=True, last_completed="2023-05-05", owner=self.user
        )

        self.data = {
            "user": self.user.id, "place": "Place Test 1", "time": "00:00", "action": "Action Test 1",
            "is_pleasant": True, "periodicity": 1, "duration": 60, "is_public": True,
            "last_completed": "2023-05-05"
        }

        response = self.client.put(f"/habit/update/{habit.id}/", data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": habit.id,
                "user": self.user.id,
                "place": "Place Test 1",
                "time": "00:00:00",
                "action": "Action Test 1",
                "is_pleasant": True,
                "link_habit": None,
                "reward": None,
                "periodicity": 1,
                "duration": 60,
                "is_public": True,
                "last_completed": "2023-05-05",
                "owner": self.user.id
            },
        )

    def test_delete_habit(self):
        """Тестирование удаления задачи"""
        habit = Habit.objects.create(
            user=self.user, place='Place Test', time='00:00', action='Action Test', is_pleasant=True, periodicity=1,
            duration=60, is_public=True, last_completed="2023-05-05", owner=self.user
        )

        response = self.client.delete(f"/habit/delete/{habit.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
