# Generated by Django 5.0.1 on 2024-01-29 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('operating_airline', models.CharField(max_length=25)),
                ('departure_city', models.CharField(max_length=25)),
                ('arrival_city', models.CharField(max_length=25)),
                ('date_of_departure', models.DateField(max_length=25)),
                ('estimated_time_of_departure', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight_app.flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight_app.passenger')),
            ],
        ),
    ]