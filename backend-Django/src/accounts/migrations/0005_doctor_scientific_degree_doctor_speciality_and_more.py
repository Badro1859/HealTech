# Generated by Django 4.1.7 on 2023-03-02 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_admin_phone_alter_doctor_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='scientific_degree',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='education degree'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Cardiologists', 'Cardiologists'), ('Neurologists', 'Neurologists'), ('Pediatricians', 'Pediatricians'), ('Physiatrists', 'Physiatrists'), ('Dermatologists', 'Dermatologists')], max_length=30, null=True, verbose_name='doctor speciality'),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('O+', 'O+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('O-', 'O-'), ('B-', 'B-'), ('AB-', 'AB-')], default='O+', max_length=15, verbose_name='blood group'),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_pressure',
            field=models.FloatField(default=0.0, help_text='Enter the patients in mmHg', verbose_name='blood pressure'),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_sugar',
            field=models.FloatField(default=0.0, help_text='Enter the patients in mg/dl', verbose_name='blood sugar'),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.FloatField(default=0.0, help_text='Enter the patients in feets', verbose_name='height'),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.FloatField(default=0.0, help_text='Enter the patients in Kgs', verbose_name='weight'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='service name')),
                ('lib', models.CharField(max_length=10, unique=True, verbose_name='libile of service')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('phone', models.CharField(blank=True, max_length=27, null=True, verbose_name='phone number')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='department_icons')),
                ('chief', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.admin')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AddField(
            model_name='admin',
            name='in_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.service'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='in_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.service'),
        ),
        migrations.AddField(
            model_name='employee',
            name='in_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.service'),
        ),
    ]
