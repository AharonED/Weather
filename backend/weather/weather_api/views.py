# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class WeatherViewSet(viewsets.ViewSet):
    # @api_view(["GET"])
    @permission_classes([IsAuthenticated])  # Optional authentication
    def list(self, request):  # /api/weather
        # products = Product.objects.all()
        # serializer = ProductSerializer(instance=products, many=True)
        return Response([{"id": "500"}], status=status.HTTP_200_OK)
