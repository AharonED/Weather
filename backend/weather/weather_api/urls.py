from django.contrib import admin
from django.urls import path

from .views import WeatherViewSet

urlpatterns = [
    path(
        "test",
        WeatherViewSet.as_view(
            {
                "get": "test",
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
    path(
        "query",
        WeatherViewSet.as_view(
            {
                "get": "query_weather_data",
            }
        ),
    ),
    path(
        "get_all_sum",
        WeatherViewSet.as_view(
            {
                "get": "get_all_sum",
            }
        ),
    ),
    path(
        "query_sum",
        WeatherViewSet.as_view(
            {
                "get": "query_sum",
            }
        ),
    ),
]
