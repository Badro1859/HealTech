# Generated by Django 4.1.7 on 2023-03-08 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.time(11, 52, 17, 202292), verbose_name='appointment time'),
        ),
    ]
