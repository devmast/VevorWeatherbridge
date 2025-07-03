from flask import Flask, request
from vevorweatherprom.classes.weather import WeatherData
from vevorweatherprom.metrics import start_prometheus_server, update_metrics
import os

app = Flask(__name__)

# Get Prometheus port from environment variable or use default 9090
PROMETHEUS_PORT = int(os.environ.get("PROMETHEUS_PORT", 9090))

@app.route('/weatherstation/updateweatherstation.php', methods=['GET'])
def update_weather_station():
    # Extract query parameters
    params = request.args.to_dict()
    print(f"Received parameters: {params}")
    
    # Process the weather data
    try:
        weather_data = WeatherData.model_validate(params, strict=False, by_alias=True, from_attributes=True)
        
        # Update Prometheus metrics
        update_metrics(weather_data)
        
        # Return a success response
        print(f"Received data: {weather_data}")
        return "success", 200
    except Exception as e:
        print(f"Error processing weather data: {e}")
        return "error", 400

def main():
    """Entry point for the application"""
    # Start Prometheus metrics server
    start_prometheus_server(PROMETHEUS_PORT)
    
    # Start Flask app
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    main()
