from flask import Flask, request, jsonify
import random

from datetime import datetime, timezone

app = Flask(__name__)

SENSOR_LOCATIONS = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen"
}

@app.route('/temperature')
def temperature():
    location = request.args.get('location', '')
    sensorID = request.args.get('sensorID', '')
    if not location:
        if sensorID == 1:
            location = "Living Room"
        elif sensorID == 2:
            location = "Bedroom"
        elif sensorID == 3:
            location = "Kitchen"
        else:
            location = "Unknown"

    if not sensorID:
        if location == "Living Room":
            sensorID = 1
        elif location == "Bedroom":
            sensorID = 2
        elif location == "Kitchen":
            sensorID = 3
        else:
            sensorID = 0

    temp = round(random.uniform(-20, 40), 2)
    return jsonify({'value': temp, 'unit': '°C', 'location': location, 'status': 'active', 'timestamp': str(datetime.now().astimezone().isoformat(timespec='seconds')), 'description': ''})

@app.route('/temperature/<sensor_id>')
def temperature_by_id(sensor_id):
    location = SENSOR_LOCATIONS.get(sensor_id, "Unknown")

    if location == "Unknown":
        return jsonify({'error': f"Sensor with id not found."})

    temp = round(random.uniform(-20, 40), 2)
    return jsonify({'value': temp, 'unit': '°C', 'location': location, 'status': 'active', 'timestamp': str(datetime.now().astimezone().isoformat(timespec='seconds')),'description': '' })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)