import asyncio
import time
from .fetch_weather_data import fetch_weather_data
from .models import WeatherEntry
from .data_processing import process_and_store_data


async def fetch_and_process_data(days):
    data = fetch_weather_data(past_days=days)
    process_and_store_data(data)


async def main():
    tasks = []
    for days in range(1, 2, 10):
        print(f"fetch_and_process_data({days})")
        tasks.append(asyncio.create_task(fetch_and_process_data(days)))
        print(f"tasks.append(create_task(fetch_and_process_data({days})))")

    await asyncio.gather(*tasks)
