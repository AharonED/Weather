from django.db.models import Avg, Min, Max
from .models import WeatherEntry, DailyWeatherSummary
from datetime import datetime


def process_and_store_data(data):
    hourly_data = data["hourly"]
    for time, temperature, humidity, wind_speed in zip(
        hourly_data["time"],
        hourly_data["temperature_2m"],
        hourly_data["relative_humidity_2m"],
        hourly_data["wind_speed_10m"],
    ):
        date_time = datetime.fromisoformat(time)
        date_only = date_time.date()

        # Create or update WeatherEntry
        entry, created = WeatherEntry.objects.get_or_create(
            date_time=date_time,
            defaults={
                "temperature": temperature,
                "relative_humidity": humidity,
                "wind_speed": wind_speed,
            },
        )

        # Currently the calculation is running for each weather data record, the code needed to be refactored,
        # to perform the calculation only once!

        # Calculate daily average temperature
        try:
            daily_summary = DailyWeatherSummary.objects.get(date=date_only)
        except DailyWeatherSummary.DoesNotExist:
            daily_summary = DailyWeatherSummary(date=date_only)
        daily_summary.average_temperature = WeatherEntry.objects.filter(
            date_time__date=date_only
        ).aggregate(Avg("temperature"))["temperature__avg"]

        daily_summary.max_temperature = WeatherEntry.objects.filter(
            date_time__date=date_only
        ).aggregate(Max("temperature"))["temperature__max"]
        daily_summary.min_temperature = WeatherEntry.objects.filter(
            date_time__date=date_only
        ).aggregate(Min("temperature"))["temperature__min"]
        daily_summary.average_temperature = WeatherEntry.objects.filter(
            date_time__date=date_only
        ).aggregate(Avg("temperature"))["temperature__avg"]

        daily_summary.save()
