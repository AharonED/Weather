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
        ordering = ["date_time"]  # Default ordering by date and time

    def __str__(self):
        return f"Date/Time: {self.date_time}, Temp: {self.temperature:.2f}°C, Humidity: {self.relative_humidity:.2f}%, Wind Speed: {self.wind_speed:.2f} km/h"
