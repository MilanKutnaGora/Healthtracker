from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from healthtrackers.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.user.set_password('123456')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place='Место',
            time='21:30:00',
            action='Действие',
            is_pleasant_habit=False,
            periodicity=1,
            reward='Вознаграждение',
            action_time=110,
            is_public=True,
        )

    def test_habit_create(self):
        data = {
            'user': self.user.id,
            'place': 'Новое место',
            'time': '19:28:00',
            'action': 'Новое действие',
            'is_pleasant_habit': False,
            'periodicity': 3,
            'reward': '',
            'action_time': 105,
            'is_public': True,
        }
        response = self.client.post(reverse('healthtrackers:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_list(self):
        response = self.client.get(reverse('healthtrackers:habit-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {
                                     'id': self.habit.id,
                                     'user': self.habit.user.id,
                                     'place': self.habit.place,
                                     'time': self.habit.time,
                                     'action': self.habit.action,
                                     'is_pleasant_habit': self.habit.is_pleasant_habit,
                                     'associated_habit': self.habit.associated_habit,
                                     'reward': self.habit.reward,
                                     'action_time': self.habit.action_time,
                                     'good_habit': self.habit.good_habit,
                                     'is_public': self.habit.is_public,
                                     'periodicity': self.habit.periodicity,

                                 }
                             ]
                         })

    def test_habit_detail(self):
        response = self.client.get(reverse('healthtrackers:habit-get', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'user': self.habit.user.id,
                             'place': self.habit.place,
                             'time': self.habit.time,
                             'action': self.habit.action,
                             'is_pleasant_habit': self.habit.is_pleasant_habit,
                             'associated_habit': self.habit.associated_habit,
                             'reward': self.habit.reward,
                             'action_time': self.habit.action_time,
                             'good_habit': self.habit.good_habit,
                             'is_public': self.habit.is_public,
                             'periodicity': self.habit.periodicity,
                         })

    def test_habit_update(self):
        data = {
            'place': 'Изменение места',
            'time': '10:45:00',
            'action': 'Изменение действия',
            'is_pleasant_habit': True,
            'periodicity': 5,
            'action_time': 60,
            'is_public': True,
        }
        response = self.client.put(reverse('healthtrackers:habit-update', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'user': self.habit.user.id,
                             'place': data['place'],
                             'time': data['time'],
                             'action': data['action'],
                             'is_pleasant_habit': data['is_pleasant_habit'],
                             'associated_habit': self.habit.associated_habit,
                             'reward': self.habit.reward,
                             'action_time': data['action_time'],
                             'good_habit': self.habit.good_habit,
                             'is_public': data['is_public'],
                             'periodicity': data['periodicity'],
                         })

    def test_habit_destroy(self):
        response = self.client.delete(reverse('healthtrackers:habit-delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_all_habits(self):
        response = self.client.get(reverse('healthtrackers:habit-all'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {
                                     'id': self.habit.id,
                                     'user': self.habit.user.id,
                                     'place': self.habit.place,
                                     'time': self.habit.time,
                                     'action': self.habit.action,
                                     'is_pleasant_habit': self.habit.is_pleasant_habit,
                                     'associated_habit': self.habit.associated_habit,
                                     'reward': self.habit.reward,
                                     'action_time': self.habit.action_time,
                                     'good_habit': self.habit.good_habit,
                                     'is_public': self.habit.is_public,
                                     'periodicity': self.habit.periodicity,

                                 }
                             ]
                         })

    def test_habit_validation(self):
        data = {
            'user': self.user.id,
            'place': 'Еще одно место',
            'time': '03:00:00',
            'action': 'Еще одно действие',
            'is_pleasant_habit': True,
            'period': 1,
            'reward': 'Еще одно вознаграждение',
            'action_time': 130,
            'is_public': True,
        }
        response = self.client.post(reverse('healthtrackers:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Время выполнения привычки должно быть не больше 120 секунд",
                                 "У приятной привычки не может быть вознаграждения или связанной привычки"
                             ]
                         })

    def tearDown(self):
        pass
