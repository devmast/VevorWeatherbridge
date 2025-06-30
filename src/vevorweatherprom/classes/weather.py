from pydantic import BaseModel, Field, computed_field

from typing import Optional, Dict, Any
from enum import Enum
from datetime import datetime
import pytz


# {'Barometric Pressure': {'value': 29.9, 'unit': 'inHg', 'device_class': 'atmospheric_pressure'}, 'Temperature': {'value': 95.0, 'unit': '°F', 'device_class': 'temperature'}, 'Humidity': {'value': '43', 'unit': '%', 'device_class': 'humidity'}, 'Dew Point': {'value': 69.0, 'unit': '°F', 'device_class': 'temperature'}, 'Rainfall': {'value': 0.0, 'unit': 'in', 'device_class': 'precipitation'}, 'Daily Rainfall': {'value': 0.0, 'unit': 'in', 'device_class': 'precipitation'}, 'Wind Direction': {'value': '76', 'unit': '°', 'device_class': None}, 'Wind Speed': {'value': 0.4, 'unit': 'mph', 'device_class': 'wind_speed'}, 'Wind Gust Speed': {'value': 0.9, 'unit': 'mph', 'device_class': 'wind_speed'}, 'UV Index': {'value': '8', 'unit': 'index', 'device_class': None}, 'Solar Radiation': {'value': '1104.0', 'unit': 'W/m²', 'device_class': 'irradiance'}}

# GET /weatherstation/updateweatherstation.php?ID=696969&PASSWORD=derp&dateutc=2025-6-30+18:1:42&baromin=29.90&tempf=93.1&humidity=44&dewptf=67.8&rainin=0&dailyrainin=0&winddir=157&windspeedmph=5.1&windgustmph=8.3&UV=9&solarRadiation=1120.0 HTTP/1.1" 200

class BarometricPressure(BaseModel):
    value: Optional[float] = Field(None, description="Barometric pressure in hPa or inHg")

class Temperature(BaseModel):
    value: Optional[float] = Field(None, description="Temperature in °C or °F")

class Humidity(BaseModel):
    value: Optional[int] = Field(None, description="Humidity percentage")

class DewPoint(BaseModel):
    value: Optional[float] = Field(None, description="Dew point in °C or °F")

class Rainfall(BaseModel):
    value: Optional[float] = Field(None, description="Rainfall in mm or in")

class DailyRainfall(BaseModel):
    value: Optional[float] = Field(None, description="Daily rainfall in mm or in")

class WindDirection(BaseModel):
    value: Optional[int] = Field(None, description="Wind direction in degrees")

class WindSpeed(BaseModel):
    value: Optional[float] = Field(None, description="Wind speed in km/h or mph")

class WindGustSpeed(BaseModel):
    value: Optional[float] = Field(None, description="Wind gust speed in km/h or mph")

class UVIndex(BaseModel):
    value: Optional[int] = Field(None, description="UV index")

class SolarRadiation(BaseModel):
    value: Optional[float] = Field(None, description="Solar radiation in W/m²")

class WeatherData(BaseModel):
    barometric_pressure: BarometricPressure = Field(..., description="Barometric pressure data")
    temperature: Temperature = Field(..., description="Temperature data")
    humidity: Humidity = Field(..., description="Humidity data")
    dew_point: DewPoint = Field(..., description="Dew point data")
    rainfall: Rainfall = Field(..., description="Rainfall data")
    daily_rainfall: DailyRainfall = Field(..., description="Daily rainfall data")
    wind_direction: WindDirection = Field(..., description="Wind direction data")
    wind_speed: WindSpeed = Field(..., description="Wind speed data")
    wind_gust_speed: WindGustSpeed = Field(..., description="Wind gust speed data")
    uv_index: UVIndex = Field(..., description="UV index data")
    solar_radiation: SolarRadiation = Field(..., description="Solar radiation data")

    # @computed_field
    # def local_time(self) -> str:
    #     return datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")