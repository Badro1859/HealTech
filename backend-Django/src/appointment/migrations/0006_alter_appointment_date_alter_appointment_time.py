# Generated by Django 4.1.7 on 2023-05-10 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.date(2023, 5, 10), verbose_name='appointment date'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.time(0, 21, 46, 856018), verbose_name='appointment time'),
        ),
    ]
