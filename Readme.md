# Бэкенд-часть SPA веб-приложения "Трекер полезных привычек"

## Установка:

* ### Убедитесь, что у вас установлен python 3.11 или более новая версия

* ### Убедитесь, что у вас установлен PostgreSQL и запущен локальный сервер базы данных

* ### Убедитесь, что у вас установлен Redis и запущен redis-сервер

## Действия по установке

1. ### Склонировать репозиторий

1. ### Создать и активировать виртуальное окружениеpython `-m venv ваша_папка_для_виртуального_окружения`

1. ### Установить зависимости командой `pip install -r requirements.txt`

1. ### Создать вашу базу данных для работы с проектом `CREATE DATABASE ваша_база_данных`;

1. ### Создать миграции через `python manage.py makemigrations` и применить их `python manage.py migrate`

1. ### Открыть командную строку и запустить `python manage.py runserver`

1. ### Для запуска Celery открыть другой экземпляр командной строки и запустить `celery -A config worker -l INFO -P eventlet`

1. ### Для запуска django-celery-beat открыть другой экземляр командной строки и запустить `celery -A config beat -l INFO`

1. ### Создать бота в телеграм

1. ### В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env

* ### _Кастомная команда для создания суперпользователя python manage.py csu_

## Используемый стек и функции:

* ### DjangoRestFramework

* ### Docs/ReDoc host://docs/ host://redoc/, работает авторизация по Bearer токену

* ### Redis

* ### Celery

* ### CORS

* ### Сервис рассылок сообщений через Telegram

* ### Пагинация для вывода списка привычек

## Алгоритм работы системы:

1. ### Зарегистрировать пользователя (POST запрос) /users/users/, ОБЯЗАТЕЛЬНО указать telegram_user_name

1. ### Получить токен пользователя (POST запрос) /users/token/

1. ### Создать привычку, при этом если это полезная  привычка is_pleasant_habit=False, то необходимо указать также вознаграждение reward, либо связанную приятную is_nice=True привычку associated_hab, а также время выполнения привычки и длительность выполнение этой привычки

1. ### При этом стоит валидация, по следующим условиям:

* #### Нельзя одновременно выбирать связанную привычку и вознаграждение

* #### Время выполнения привычки не должно быть больше 120 секунд

* #### В связанные привычки могут попадать только привычки с признаком приятной привычки

* #### У приятной привычки не может быть вознаграждения или связанной привычки

* #### Нельзя выполнять привычку реже, чем 1 раз в 7 дней

* #### Если в привычке указать is_public=True, то она будет доступна в списке всех публичных привычек для других пользователей

5. ### После создания привычек отрабатывает функция, которая проверяет время и если время совпадает с текущим - отправляет уведомление в Telegram для пользователя

## Права доступа:

* ### Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.

* ### Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

## Эндпоинты:

* ### Регистрация пользователя

* ### Просмотр деталей профиля

* ### Редактирование профиля

* ### Получение токена

* ### Обновление токена

* ### Список публичных привычек

* ### Список своих привычек с пагинацией

* ### Создание привычки

* ### Редактирование привычки(через PUT)

* ### Удаление привычки