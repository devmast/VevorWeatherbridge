from flask import Flask, request
from vevorweatherprom.classes.weather import WeatherData
from vevorweatherprom.metrics import start_prometheus_server, update_metrics
import os
import argparse

app = Flask(__name__)

# Default settings
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 80
DEFAULT_PROMETHEUS_PORT = 9090

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

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='VEVOR Weather Station to Prometheus Bridge')
    
    # Flask server settings
    parser.add_argument('--host', type=str, default=os.environ.get('HOST', DEFAULT_HOST),
                        help=f'Host address to listen on (default: {DEFAULT_HOST})')
    parser.add_argument('--port', type=int, default=int(os.environ.get('PORT', DEFAULT_PORT)),
                        help=f'Port to listen on (default: {DEFAULT_PORT})')
    
    # Prometheus settings
    parser.add_argument('--prometheus-port', type=int, 
                        default=int(os.environ.get('PROMETHEUS_PORT', DEFAULT_PROMETHEUS_PORT)),
                        help=f'Port for Prometheus metrics server (default: {DEFAULT_PROMETHEUS_PORT})')
    
    # Debug mode
    parser.add_argument('--debug', action='store_true',
                        help='Run Flask in debug mode')
    
    return parser.parse_args()

def main():
    """Entry point for the application"""
    # Parse command line arguments
    args = parse_args()
    
    # Start Prometheus metrics server
    start_prometheus_server(args.prometheus_port)
    print(f"Prometheus metrics server started on port {args.prometheus_port}")
    
    # Start Flask app
    print(f"Starting Flask server on {args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()
