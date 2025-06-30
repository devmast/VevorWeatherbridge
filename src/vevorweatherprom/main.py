from flask import Flask, request
from vevorweatherprom.classes.weather import WeatherData

app = Flask(__name__)

@app.route('/weatherstation/updateweatherstation.php', methods=['GET'])
def update_weather_station():
    # Extract query parameters
    params = request.args.to_dict()
    print(f"Received parameters: {params}")
    # Process the weather data
    weather_data = WeatherData.model_validate(params, strict=False, by_alias=True, from_attributes=True)
    # Return a success response
    print(f"Received data: {weather_data}")
    return "success", 200

def main():
    """Entry point for the application"""
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    main()
