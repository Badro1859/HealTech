# Generated by Django 4.1.7 on 2023-03-06 10:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='appointment date')),
                ('time', models.TimeField(default=datetime.time(11, 30, 52, 659201), verbose_name='appointment time')),
                ('status', models.CharField(choices=[('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Pending', 'Pending'), ('Expired', 'Expired')], default='Pending', max_length=20, verbose_name='status')),
                ('doctor_notes', models.TextField(blank=True, help_text='Signs  & Symptoms.', null=True, verbose_name='medical notes')),
                ('patient_notes', models.TextField(blank=True, help_text='Please, describe your problem.', null=True, verbose_name='your message')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.doctor')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.employee')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.service')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
                'ordering': ('-date', '-time'),
            },
        ),
    ]
