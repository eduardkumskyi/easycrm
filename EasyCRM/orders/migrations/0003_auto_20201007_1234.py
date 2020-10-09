# Generated by Django 2.2 on 2020-10-07 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201006_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pay_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]