# Generated by Django 2.2 on 2020-10-09 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Project', verbose_name='Проект'),
        ),
    ]
