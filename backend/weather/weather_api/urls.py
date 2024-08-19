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
]
