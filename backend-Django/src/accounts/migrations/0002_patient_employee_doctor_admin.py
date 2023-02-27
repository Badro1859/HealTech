# Generated by Django 4.1.7 on 2023-02-27 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20, verbose_name='gender')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='phone number')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20, verbose_name='gender')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='phone number')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20, verbose_name='gender')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='phone number')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20, verbose_name='gender')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='phone number')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
