# Generated by Django 4.1.7 on 2023-02-27 21:40

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_patient_employee_doctor_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
