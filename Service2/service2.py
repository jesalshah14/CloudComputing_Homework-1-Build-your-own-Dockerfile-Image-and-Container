from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def weather():
    
    zip_code = request.args.get("zip")
    api_key = "828e27fa703c4550bd42a66963dc073a"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}"
    weather_data = requests.get(weather_url).json()
    return weather_data

if __name__ == "__main__":
    app.run(debug=True)
