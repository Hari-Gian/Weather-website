from flask import Flask, request, jsonify
from weather import Weather
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/weather", methods=["GET"])
def weather_endpoint():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "no city given"}), 400
    
    data = Weather(city)
    if not data:
        return jsonify({"error": "city not found"}), 404
    
    return jsonify(data)  

if __name__ == "__main__":
    app.run(debug=True)
