from django.db import models


# Weather
class WeatherEntry(models.Model):
    date_time = models.DateTimeField(primary_key=True)
    temperature = (
        models.FloatField()
    )  # °C (°F)	    Air temperature at 2 meters above ground
    relative_humidity = (
        models.FloatField()
    )  # %	        Relative humidity at 2 meters above ground
    wind_speed = models.FloatField()  # km/h        Wind speed at 10 meters above ground

    class Meta:
        db_table = "WeatherEntry"
        ordering = ["date_time"]  # Default ordering by date and time

    def __str__(self):
        return f"Date/Time: {self.date_time}, Temp: {self.temperature:.2f}°C, Humidity: {self.relative_humidity:.2f}%, Wind Speed: {self.wind_speed:.2f} km/h"


class DailyWeatherSummary(models.Model):
    date = models.DateField(primary_key=True)
    average_temperature = models.FloatField(default=None, blank=True, null=True)
    max_temperature = models.FloatField(default=None, blank=True, null=True)
    min_temperature = models.FloatField(default=None, blank=True, null=True)

    class Meta:
        db_table = "DailyWeatherSummary"
        ordering = ["date"]  # Default ordering by date and time


# For deleting all data using shell consol:
# python manage.py shell
# from django.db import models
# from weather_data_service.models import DailyWeatherSummary
# DailyWeatherSummary.objects.all().delete()
