# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import WeatherEntry
from .serializers import WeatherEntrySerializer
import asyncio
from .async_tasks import main


class WeatherViewSet(viewsets.ViewSet):
    # @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def list(self, request):  # /api/weather
        asyncio.run(main())
        weather = WeatherEntry.objects.all()
        serializer = WeatherEntrySerializer(instance=weather, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
