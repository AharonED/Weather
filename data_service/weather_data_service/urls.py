from django.contrib import admin
from django.urls import path

from .views import WeatherViewSet

urlpatterns = [
    path(
        "fetch",
        WeatherViewSet.as_view(
            {
                "get": "fetch",
            }
        ),
    ),
]
