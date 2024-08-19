import requests
from datetime import datetime

# API URL with your desired parameters
API_URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&past_days={past_days}&hourly={hourly_parameters}"


# Function to fetch weather data for a given location
def fetch_weather_data(
    latitude,
    longitude,
    past_days=10,
    hourly_parameters="temperature_2m,relative_humidity_2m,wind_speed_10m",
):
    url = API_URL.format(
        latitude=latitude,
        longitude=longitude,
        past_days=past_days,
        hourly_parameters=hourly_parameters,
    )
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    return data


# # Example usage with your location
# if __name__ == "__main__":
#     weather_data = fetch_weather_data(latitude=52.52, longitude=13.41)
#     print(weather_data)  # Example output: (refer to provided data model)
