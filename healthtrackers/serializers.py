from rest_framework import serializers

from healthtrackers.models import Habit
from healthtrackers.validators import RewardAndHabitValidator, ActionTimeValidator, IsPleasantValidator, PleasantHabitValidator, PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            RewardAndHabitValidator(reward='reward', habit='associated_habit'),
            ActionTimeValidator(time='action_time'),
            IsPleasantValidator(habit='associated_habit'),
            PleasantHabitValidator(very_is_pleasant_habit='is_pleasant_habit', reward='reward', habit='associated_habit'),
            PeriodValidator(periodicity='periodicity')
        ]