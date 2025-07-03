from prometheus_client import Gauge, start_http_server
import os

# Dictionary to store our gauge metrics
gauges = {}

# Create gauges for weather measurements
barometric_pressure_gauge = Gauge('weather_barometric_pressure', 'Barometric pressure in inHg or hPa')
temperature_gauge = Gauge('weather_temperature', 'Temperature in °F or °C')
humidity_gauge = Gauge('weather_humidity', 'Humidity percentage')
dew_point_gauge = Gauge('weather_dew_point', 'Dew point in °F or °C')
rainfall_gauge = Gauge('weather_rainfall', 'Rainfall in in or mm')
daily_rainfall_gauge = Gauge('weather_daily_rainfall', 'Daily rainfall in in or mm')
wind_direction_gauge = Gauge('weather_wind_direction', 'Wind direction in degrees')
wind_speed_gauge = Gauge('weather_wind_speed', 'Wind speed in mph or km/h')
wind_gust_speed_gauge = Gauge('weather_wind_gust_speed', 'Wind gust speed in mph or km/h')
uv_index_gauge = Gauge('weather_uv_index', 'UV index')
solar_radiation_gauge = Gauge('weather_solar_radiation', 'Solar radiation in W/m²')

# Store all gauges in a dictionary for easy access
gauges = {
    'barometric_pressure': barometric_pressure_gauge,
    'temperature': temperature_gauge,
    'humidity': humidity_gauge,
    'dew_point': dew_point_gauge,
    'rainfall': rainfall_gauge,
    'daily_rainfall': daily_rainfall_gauge,
    'wind_direction': wind_direction_gauge,
    'wind_speed': wind_speed_gauge,
    'wind_gust_speed': wind_gust_speed_gauge,
    'uv_index': uv_index_gauge,
    'solar_radiation': solar_radiation_gauge,
}

def start_prometheus_server(port=9090):
    """Start the Prometheus metrics server on the specified port"""
    start_http_server(port)
    print(f"Prometheus metrics server started on port {port}")

def update_metrics(weather_data):
    """Update Prometheus metrics with values from WeatherData object"""
    # Update each gauge with the corresponding value from weather_data
    for metric_name, gauge in gauges.items():
        # Get the value from the weather_data object
        value = getattr(weather_data, metric_name)
        
        # Only update if the value is not None
        if value is not None:
            gauge.set(value)