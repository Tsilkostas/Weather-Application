# Generated by Django 5.0.7 on 2024-08-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('station_id', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.CharField(max_length=10)),
                ('rain_gauge', models.FloatField()),
            ],
        ),
    ]
