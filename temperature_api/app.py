from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/temperature')
def temperature():
    location = request.args.get('location', '')
    sensorID = request.args.get('sensorID', '')
    if not location:
        if sensorID == "1":
            location = "Living Room"
        elif sensorID == "2":
            location = "Bedroom"
        elif sensorID == "3":
            location = "Kitchen"
        else:
            location = "Unknown"

    if not sensorID:
        if location == "Living Room":
            sensorID = "1"
        elif location == "Bedroom":
            sensorID = "2"
        elif location == "Kitchen":
            sensorID = "3"
        else:
            sensorID = "0"

    temp = round(random.uniform(-20, 40), 2)
    return jsonify({'location': location, 'sensor': sensorID, 'temperature': temp})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)