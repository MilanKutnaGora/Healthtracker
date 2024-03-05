from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    chat_id = models.TextField(verbose_name='id чата в телеграмме', **NULLABLE)
    telegram_user_name = models.CharField(max_length=250, verbose_name='имя в телеграмме', unique=True, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
