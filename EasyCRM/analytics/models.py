from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from crm.models import Project


User = get_user_model()

TYPES = (
        (1, 'Расход'),
        (2, 'Доход'),
    )


class Purpose(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    type = models.IntegerField(verbose_name='Тип', choices=TYPES, default='1')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'


class Transaction(models.Model):

    type = models.IntegerField(verbose_name='Тип', choices=TYPES, default='1')
    purpose = models.ForeignKey(Purpose, verbose_name='Назначение', on_delete=models.CASCADE, blank=True)
    sum = models.IntegerField(verbose_name='Сумма', default=0)
    comment = models.CharField(verbose_name='Комментарий', max_length=150, blank=True)
    date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.purpose} ({self.sum})"

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
