# DRF_Project — бэкенд для приложения курсов

## Описание:

Приложение позволяет добавлять курсы и уроки к ним, а также оплачивать их с помощью стороннего сервиса

## Установка:

Рекомендуется использовать PyCharm

Ссылка для добавления проекта
https://github.com/DanilaYukin/project_DRF

## Использование:

Перед началом использования создайте миграции с помощью команды python manage.py makemigrations

Далее нужно их применить с помощью команды python manage.py migrate
Для запуска используйте команду python manage.py runserver

Также можно воспользоваться Docker и собрать все в контейнеры для совместной работы с помощью Docker Compose
Для этого в терминале используйте команду

```commandline
docker-compose up -d --build
```

Для проверки работоспособности контейнера postgres выполните команду:

```commandline
docker exec db pg_isready -U postgres
```

Для проверки работоспособности контейнера celery выполните команду:

```commandline
docker-compose exec celery celery -A config.celery status 
```

Также можно проверить через логи:

```commandline
docker-compose logs celery --tail=50
```

Для проверки работоспособности контейнера celery-beat выполните команду:

```commandline
docker-compose logs celery-beat --tail=50
```

Для проверки работоспособности контейнера redis выполните команду:

```commandline
docker-compose logs redis --tail=10
```

Для проверки работоспособности контейнера web выполните команду:

```commandline
docker-compose logs web --tail=20
```

## Функционал

Функционал содержится в 3-ех модулях

Модули:

1. `config` - настройки проекта
2. `lms` - директория курсов и уроков
3. `users` - директория пользователей


##  Доступ к развернутому приложению

Приложение доступно по адресу:

**http://158.160.187.45//**
---

##  Установка и запуск локально

1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/DanilaYukin/TreckerProject.git
   cd TreckerProject
   
Создай виртуальное окружение и установи зависимости:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Создай файл .env в корне проекта со своими переменными окружения:
    
    makefile
    Копировать код
    SECRET_KEY=твой_secret_key
    DEBUG=True
    DATABASE_URL=...
    CELERY_BROKER_URL=...
    ...

Примените миграции и соберите статические файлы:
    
    bash
    Копировать код
    python manage.py migrate
    python manage.py collectstatic --noinput
    Запуск:
    
    bash
    Копировать код
    python manage.py runserver
    ```

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)