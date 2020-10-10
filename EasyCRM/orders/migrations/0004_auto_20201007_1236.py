# Generated by Django 2.2 on 2020-10-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201007_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'Переговоры'), (3, 'Ожидается оплата'), (4, 'В производстве'), (5, 'Ожидает отгрузку'), (6, 'В пути'), (7, 'В отделении'), (8, 'Оплачен'), (9, 'Отказ на почте'), (10, 'Отмена'), (11, 'Возврат/Обмен')], default='1', verbose_name='Статус'),
        ),
    ]
