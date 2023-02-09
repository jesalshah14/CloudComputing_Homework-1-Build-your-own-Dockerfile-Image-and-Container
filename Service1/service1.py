# zip_api.py
from flask import Flask, request
import requests

app = Flask(__name__)

# Example dictionary to store zip codes for cities
zip_codes = {
    "New York": "10001",
    "Los Angeles": "90001",
    "Chicago": "60601",
    "Newark" : "94560",
    "Fremont" : "94550"
}

@app.route('/zip/<string:city>', methods=['GET'])
def zip_api(city):
    if city in zip_codes:
        zip_code = str(zip_codes[city])
        # Send a request to the second API to get the weather for the zip code
        weather_api_response = requests.get(f'http://weatherservice:5001/weather/{zip_code}')
        weather = weather_api_response.text
        return f' The weather in {city}({zip_code}) is   - <b>{weather}'
    else:
        return 'City not found'

if __name__ == '__main__':
    app.run()
    
    
    
    # http://localhost:5001/weather/10001  http://localhost:5001/weather?zip=94560
    
    # http://localhost:5000/zip/New York      http://localhost:5000/zipcode?city=Chicago