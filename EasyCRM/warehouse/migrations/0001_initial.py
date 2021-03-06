# Generated by Django 2.2 on 2021-01-25 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Тип товара',
                'verbose_name_plural': 'Типы товара',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('in_stock', models.IntegerField(verbose_name='Кол-во')),
                ('unit', models.IntegerField(choices=[(1, 'м.'), (2, 'кг'), (3, 'шт.'), (4, 'уп.')], default='1', verbose_name='Ед. измерения')),
                ('standard_price', models.IntegerField(verbose_name='Стандартная стоимость')),
                ('sale_price', models.IntegerField(verbose_name='Акционная стоимость')),
                ('wholesale_price', models.IntegerField(verbose_name='Оптовая стоимость')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.ProductSize', verbose_name='Размер')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.ProductType', verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='PrimaryProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Тип товара',
                'verbose_name_plural': 'Типы товара',
            },
        ),
        migrations.CreateModel(
            name='PrimaryProductSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('phone', models.CharField(max_length=150, verbose_name='Телефон')),
                ('link', models.CharField(max_length=150, verbose_name='Ссылка')),
                ('comment', models.CharField(max_length=150, verbose_name='Комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='PrimaryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('in_stock', models.IntegerField(verbose_name='Кол-во')),
                ('unit', models.IntegerField(choices=[(1, 'м.'), (2, 'кг'), (3, 'шт.'), (4, 'уп.')], default='1', verbose_name='Ед. измерения')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('date_of_receiving', models.DateTimeField(blank=True, verbose_name='Дата получения')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.PrimaryProductSupplier', verbose_name='Поставщик')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.PrimaryProductType', verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сырье',
            },
        ),
    ]
