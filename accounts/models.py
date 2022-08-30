from django.db import models
from django.contrib.auth.models import AbstractUser


AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('username').blank = True
AbstractUser._meta.get_field('username')._unique = False

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'