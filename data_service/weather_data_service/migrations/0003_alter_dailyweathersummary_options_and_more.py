# Generated by Django 5.1 on 2024-08-20 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data_service', '0002_dailyweathersummary_weatherentry_delete_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyweathersummary',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelTable(
            name='dailyweathersummary',
            table='DailyWeatherSummary',
        ),
        migrations.AlterModelTable(
            name='weatherentry',
            table='WeatherEntry',
        ),
    ]
