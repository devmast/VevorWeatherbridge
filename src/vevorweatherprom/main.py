from flask import Flask, request
from ..classes.weather import WeatherData

app = Flask(__name__)

@app.route('/weatherstation/updateweatherstation.php', methods=['GET'])
def update_weather_station():
    # Extract query parameters
    params = request.args.to_dict()
    # Process the weather data
    weather_data = WeatherData(**params)
    # Return a success response
    print(f"Received data: {weather_data}")
    return "success", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
