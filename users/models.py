from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="номер телефона"
    )
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="фото"
    )
    country = models.CharField(max_length=50, blank=True, verbose_name="страна")
    tg_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name="tg_id",
        help_text="введите ваш tg_id",
    )
    tg_chat_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name="chat_id",
        help_text="введите ваш chat_id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
