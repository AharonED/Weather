from django.test import TestCase
from rest_framework.test import APIClient
from .models import WeatherData, DailyWeatherSummary
from datetime import datetime, timedelta


# Test cases for API endpoints and scenarios


# Navigate to your project's root directory, and Run the following command:
# python manage.py test weather_api
class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample weather data
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 1, 10)
        delta = timedelta(days=1)
        while start_date <= end_date:
            WeatherData.objects.create(
                date=start_date,
                temperature=20 + start_date.day,
                humidity=50 + start_date.day,
                wind_speed=10 + start_date.day,
            )
            start_date += delta

    def test_get_all_weather_data(self):
        response = self.client.get("/api/weather/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)  # Assuming 10 data entries

    def test_query_weather_data_by_date_range(self):
        response = self.client.get(
            "/api/weather/query/?date_from=2023-01-05&date_to=2023-01-08"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_query_weather_data_invalid_date_range(self):
        response = self.client.get(
            "/api/weather/query/?date_from=2024-01-01&date_to=2023-01-01"
        )
        self.assertEqual(
            response.status_code, 400
        )  # Assuming you're handling invalid date ranges appropriately

    # def test_data_processing_and_storage(self):
    #     # Trigger data processing (e.g., by calling a management command)
    #     # ...

    #     # Verify data is stored in WeatherData and DailyWeatherSummary
    #     self.assertEqual(WeatherData.objects.count(), 10)
    #     self.assertEqual(DailyWeatherSummary.objects.count(), 10)

    #     # Check aggregated data accuracy
    #     daily_summary = DailyWeatherSummary.objects.get(date=datetime.date(2023, 1, 1))
    #     self.assertEqual(daily_summary.average_temperature, 20)
    #     # ... other assertions for aggregated data
