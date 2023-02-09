# weather_api.py
from flask import Flask, request
app = Flask(__name__)

# Example dictionary to store weather information for zip codes
weather = {
    '10001': 'Description : Clear Sky, Temperature: 72, Humidity:30, Main:Clear',
    '60601': 'Description : Freezing Rain, Temperature: 50, Humidity:20, Main:Rainy',
    '90001': 'Description : Snow Showers, Temperature: 80, Humidity:25, Main:Snow',
    '94560': 'Description : Partly Cloud, Temperature: 40, Humidity:18, Main:Cloudy',
    '94550': 'Description : Mostly Sunny, Temperature: 90, Humidity:18, Main:Sunny'
}

@app.route('/weather/<string:zip_code>', methods=['GET'])
def weather_api(zip_code):
    if zip_code in weather:
        return weather[zip_code]
    else:
        return 'Weather information not available for the given zip code'

if __name__ == '__main__':
    app.run(port=5001)