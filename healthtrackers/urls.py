from django.urls import path

from healthtrackers.apps import HealthtrackersConfig
from healthtrackers.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView, HabitAllAPIView

app_name = HealthtrackersConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('all/', HabitAllAPIView.as_view(), name='habit-all'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit-delete'),
]