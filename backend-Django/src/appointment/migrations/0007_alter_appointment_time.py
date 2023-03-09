# Generated by Django 4.1.7 on 2023-03-09 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0006_alter_appointment_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="time",
            field=models.TimeField(
                default=datetime.time(8, 11, 4, 50931), verbose_name="appointment time"
            ),
        ),
    ]
