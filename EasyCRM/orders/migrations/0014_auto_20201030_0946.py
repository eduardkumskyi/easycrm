# Generated by Django 2.2 on 2020-10-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20201010_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message_1',
            field=models.BooleanField(default=False, verbose_name='Сообщение №1'),
        ),
        migrations.AddField(
            model_name='order',
            name='message_2',
            field=models.BooleanField(default=False, verbose_name='Сообщение №2'),
        ),
        migrations.AddField(
            model_name='order',
            name='message_3',
            field=models.BooleanField(default=False, verbose_name='Сообщение №3'),
        ),
    ]
