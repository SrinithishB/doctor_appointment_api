# Generated by Django 5.0.4 on 2024-04-20 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('appointment_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('max_patients', models.PositiveIntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
    ]