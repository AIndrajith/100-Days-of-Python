# defining API routes and Endpoints

from flask import Flask, jsonify, request

app = Flask(__name__)

# Modk Weather Data
weather_data = {
    "new york":{"temperature":22, "condition":"sunny"},
    "london": {"temperature":15, "condition":"Cloudy"},
    "tokyo": {"temperature":28, "condition":"Clear"}
}

# Roo Endpoint
@app.route('/')
def home():
    return jsonify({"message":"Welcome to the Mini Weather API!"})

# Get Weather for all cities
@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

# Get Weather for a specific City
@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error":"city not found"}), 404

# Run App
if __name__=='__main__':
    app.run(debug=True)

# Returning JSON Responses
# in here we can see the responses