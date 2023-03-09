# Generated by Django 4.1.7 on 2023-03-08 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0003_alter_appointment_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="time",
            field=models.TimeField(
                default=datetime.time(23, 46, 8, 840118),
                verbose_name="appointment time",
            ),
        ),
    ]
