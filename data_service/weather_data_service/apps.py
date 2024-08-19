from django.apps import AppConfig
import asyncio

# from .async_tasks import main

# import django


class WeatherDataServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "weather_data_service"

    # def ready(self):
    #     # django.setup()
    #     if not self.loaded:
    #         asyncio.run(main())
