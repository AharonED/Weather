from django.contrib import admin
from django.urls import path

from .views import WeatherViewSet

urlpatterns = [
    path(
        "weather",
        WeatherViewSet.as_view(
            {
                "get": "list",
            }
        ),
    ),
    path(
        "get_all",
        WeatherViewSet.as_view(
            {
                "get": "get_all_weather_data",
            }
        ),
    ),
]
