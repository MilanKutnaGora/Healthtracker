from rest_framework.exceptions import ValidationError


class RewardAndHabitValidator:
    def __init__(self, reward, habit):
        self.reward = reward
        self.habit = habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        habit = dict(value).get(self.habit)
        if reward and habit:
            raise ValidationError('Не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки')


class ActionTimeValidator:
    def __init__(self, time):
        self.time = time

    def __call__(self, value):
        time = dict(value).get(self.time)
        if time > 120:
            raise ValidationError('Время выполнения привычки должно быть не больше 120 секунд')


class IsPleasantValidator:
    def __init__(self, habit):
        self.habit = habit

    def __call__(self, value):
        if value.get(self.habit):
            is_pleasant_habit = dict(value).get(self.habit).is_pleasant_habit
            if not is_pleasant_habit:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class PleasantHabitValidator:
    def __init__(self, very_is_pleasant_habit, reward, habit):
        self.very_is_pleasant_habit = very_is_pleasant_habit
        self.reward = reward
        self.habit = habit

    def __call__(self, value):
        very_is_pleasant_habit = dict(value).get(self.very_is_pleasant_habit)
        reward = dict(value).get(self.reward)
        habit = dict(value).get(self.habit)
        if very_is_pleasant_habit:
            if reward or habit:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodValidator:
    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        periodicity = dict(value).get(self.periodicity)
        if periodicity < 1:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')