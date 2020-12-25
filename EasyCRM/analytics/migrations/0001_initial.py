# Generated by Django 2.2 on 2020-12-25 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('type', models.IntegerField(choices=[(1, 'Расход'), (2, 'Доход')], default='1', verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Назначение транзакции',
                'verbose_name_plural': 'Назначения транзакций',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Расход'), (2, 'Доход')], default='1', verbose_name='Тип')),
                ('sum', models.IntegerField(default=0, verbose_name='Сумма')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Project', verbose_name='Проект')),
                ('purpose', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='analytics.Purpose')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Транзацкция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]
