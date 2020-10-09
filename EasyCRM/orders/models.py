from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Project(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    country = models.CharField(verbose_name='Страна', max_length=150, blank=True)
    np_api = models.CharField(verbose_name='API ключ "Новая Почта', max_length=150, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150, blank=True)
    second_name = models.CharField(verbose_name='Фамилия', max_length=150, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    phone = models.IntegerField(verbose_name='Телефон', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=150, blank=True)
    department = models.CharField(verbose_name='Отделение', max_length=150, blank=True)
    waybill = models.IntegerField(verbose_name='ТТН', null=True, unique=True, blank=True)
    order = models.TextField(verbose_name='Заказ', max_length=250, blank=True)
    comment = models.TextField(verbose_name='Комментарий', max_length=250, blank=True)
    STATES = (
        (1, 'Новый'),
        (2, 'Переговоры'),
        (3, 'Ожидается оплата'),
        (4, 'В производстве'),
        (5, 'Ожидает отгрузку'),
        (6, 'В пути'),
        (7, 'В отделении'),
        (8, 'Оплачен'),
        (9, 'Отказ на почте'),
        (10, 'Отмена'),
        (11, 'Возврат/Обмен'),
    )
    state = models.IntegerField(verbose_name='Статус', choices=STATES, default='1')
    price = models.IntegerField(verbose_name='Сумма', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now, blank=True)
    update_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='Проект', default=1, on_delete=models.CASCADE)
