from rest_framework import serializers
from .models import WeatherEntry, DailyWeatherSummary


class WeatherEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherEntry
        fields = "__all__"


class DailyWeatherSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWeatherSummary
        fields = "__all__"
