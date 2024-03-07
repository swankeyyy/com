from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/photo/", blank=True, null=True, verbose_name="Фото профиля")
    date_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    phone = models.IntegerField(verbose_name="Номер телефона", null=True, blank=True, default=0)
    adress = models.CharField(max_length=200, verbose_name="Адрес доставки", null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


