import requests
from datetime import datetime

# We use https://open-meteo.com - Free Weather API, to retrive weather data.
# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
# 	"latitude": 52.52,
# 	"longitude": 13.41,
# 	"hourly": "temperature_2m"
# }
# Variable	            Unit	    Description
# temperature_2m		°C (°F)	    Air temperature at 2 meters above ground
# relative_humidity_2m  %	        Relative humidity at 2 meters above ground
# wind_direction_10m

# API return value:
# On success a JSON object will be returned for instance:
#
# https://api.open-meteo.com/v1/forecast?latitude=31.5&longitude=34.75&past_days=10&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m
#
# {"latitude":31.5,"longitude":34.75,"generationtime_ms":8.02600383758545,
# "utc_offset_seconds":0,"timezone":"GMT", "timezone_abbreviation":"GMT","elevation":170.0,
# "hourly_units":{"time":"iso8601","temperature_2m":"°C","relative_humidity_2m":"%","wind_speed_10m":"km/h"},
#  "hourly": {
#     "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
#     "temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...],
#     "relative_humidity_2m":[93,92,91,92,86,77,66,58,51, ...],
#     "wind_speed_10m":[4.3,4.6,4.6,5.1,5.9,7.6,9.1,10.7,12.3,14.0, ...]
#   }}


# API URL with desired parameters
API_URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&past_days={past_days}&hourly={hourly_parameters}"


# Function to fetch weather data for a given location
# Example usage:
#     weather_data = fetch_weather_data(latitude=52.52, longitude=13.41)
def fetch_weather_data(
    latitude=31.5,
    longitude=34.75,
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
