# Generated by Django 2.2 on 2020-12-25 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('country', models.CharField(blank=True, max_length=150, verbose_name='Страна')),
                ('np_api', models.CharField(blank=True, max_length=150, verbose_name='API ключ Новая Почта')),
                ('turbosms_api', models.CharField(blank=True, max_length=150, verbose_name='API ключ TurboSMS')),
                ('turbosms_sender', models.CharField(blank=True, max_length=150, verbose_name='Подпись TurboSMS')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=150, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=150, verbose_name='Телефон')),
                ('city', models.CharField(blank=True, max_length=150, verbose_name='Город')),
                ('department', models.CharField(blank=True, max_length=150, verbose_name='Отделение')),
                ('waybill', models.CharField(blank=True, max_length=150, verbose_name='Номер накладной')),
                ('order', models.TextField(blank=True, max_length=250, verbose_name='Заказ')),
                ('comment', models.TextField(blank=True, max_length=250, verbose_name='Комментарий')),
                ('state', models.IntegerField(choices=[(1, 'Новый'), (2, 'Переговоры'), (3, 'Ожидается оплата'), (4, 'В производстве'), (5, 'Ожидает отгрузку'), (6, 'В пути'), (7, 'В отделении'), (8, 'Оплачен'), (9, 'Отказ на почте'), (10, 'Отмена'), (11, 'Возврат/Обмен')], default='1', verbose_name='Статус')),
                ('sum', models.IntegerField(blank=True, null=True, verbose_name='Сумма заказа')),
                ('payed_sum', models.IntegerField(blank=True, null=True, verbose_name='Оплачено')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('message_1', models.BooleanField(default=False, verbose_name='Сообщение №1')),
                ('message_2', models.BooleanField(default=False, verbose_name='Сообщение №2')),
                ('message_3', models.BooleanField(default=False, verbose_name='Сообщение №3')),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crm.Project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
