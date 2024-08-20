# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q  # for filtering

from .models import WeatherEntry
from .serializers import WeatherEntrySerializer


class WeatherViewSet(viewsets.ViewSet):
    # @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def list(self, request):  # /api/weather
        return Response([{"id": "500"}], status=status.HTTP_200_OK)

    # @api_view(["GET"])
    # @permission_classes([IsAuthenticated])
    def get_all_weather_data(self, request):
        weather_data = WeatherEntry.objects.all().order_by("-date_time")
        serializer = WeatherEntrySerializer(weather_data, many=True)
        return Response(serializer.data)

    # @api_view(["GET"])
    # @permission_classes([IsAuthenticated])
    def query_weather_data(self, request):
        # /api/query?start_date=2024-08-15&end_date=2024-08-19
        # Implement filtering based on request parameters (date range, thresholds)
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        min_temperature = request.GET.get("min_temperature")
        max_temperature = request.GET.get("max_temperature")

        filters = Q()
        if start_date and end_date:
            filters &= Q(date_time__gte=start_date, date_time__lte=end_date)
        if min_temperature:
            filters &= Q(temperature__gte=min_temperature)
        if max_temperature:
            filters &= Q(temperature__lte=max_temperature)

        weather_data = WeatherEntry.objects.filter(filters).order_by("-date_time")
        serializer = WeatherEntrySerializer(weather_data, many=True)
        return Response(serializer.data)
