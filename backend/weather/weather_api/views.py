# from django.shortcuts import render
from datetime import datetime
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q  # for filtering

from .models import WeatherEntry, DailyWeatherSummary
from .serializers import WeatherEntrySerializer, DailyWeatherSummarySerializer


class WeatherViewSet(viewsets.ViewSet):
    # @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def test(self, request):  # /api/test
        return Response([{"id": "100"}], status=status.HTTP_200_OK)

    # /api/get_all
    # @api_view(["GET"])
    # @permission_classes([IsAuthenticated])
    def get_all_weather_data(self, request):
        weather_data = WeatherEntry.objects.all().order_by("-date_time")
        serializer = WeatherEntrySerializer(weather_data, many=True)
        return Response(serializer.data)

    # /api/query
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

    # /api/get_all_sum
    def get_all_sum(self, request):
        daily_sum = DailyWeatherSummary.objects.all().order_by("-date")
        sum_serializer = DailyWeatherSummarySerializer(daily_sum, many=True)
        return Response(sum_serializer.data)

    # api/query_sum
    def query_sum(self, request):
        """
        Query DailyWeatherSummary data based on request parameters (optional).
        """
        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)

        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            summaries = DailyWeatherSummary.objects.filter(
                date__range=(start_date, end_date)
            )
        else:
            summaries = DailyWeatherSummary.objects.all()

        serializer = DailyWeatherSummarySerializer(summaries, many=True)
        return Response(serializer.data)
