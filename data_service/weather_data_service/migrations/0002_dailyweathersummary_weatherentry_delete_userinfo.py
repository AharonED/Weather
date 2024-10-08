# Generated by Django 5.1 on 2024-08-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWeatherSummary',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('average_temperature', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherEntry',
            fields=[
                ('date_time', models.DateTimeField(primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('relative_humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
            ],
            options={
                'ordering': ['date_time'],
            },
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
