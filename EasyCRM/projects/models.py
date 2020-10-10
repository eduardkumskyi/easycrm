from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    country = models.CharField(verbose_name='Страна', max_length=150, blank=True)
    np_api = models.CharField(verbose_name='API ключ "Новая Почта', max_length=150, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
