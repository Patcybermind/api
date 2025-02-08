from flask import Flask, jsonify, request, send_from_directory
import json
from datetime import datetime

app = Flask(__name__)

sensor_data = {
    'temperature': 25,
    'humidity': 50,
    'gps': {
        'latitude': 37.77,
        'longitude': -122.42
    }
}

entry_counter = 0

@app.route('/get-sensor-data', methods=['GET']) # includes things like temperature, humidity, gps coordinates height etc.
def get_sensor_data():
    return jsonify(sensor_data)

@app.route('/post-sensor-data', methods=['POST'])
def post_data():
    global sensor_data
    sensor_data = request.get_json()
    print(sensor_data)

    global entry_counter
    
    # Load the existing data from the JSON file
    with open('sensor_data.json', 'r') as file:
        data = json.load(file)
    
    # add the new entry and the time 
    data[entry_counter] = {
        'timestamp': datetime.now().isoformat(),
        'data': sensor_data
    }
    
    
    with open('sensor_data.json', 'w') as file:
        json.dump(data, file, indent=4)

    
        
    entry_counter += 1
    return jsonify(sensor_data), 201


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files["file"]
    
    if file.filename == "":
        return "No selected file", 400
    
    # Save the file or process it
    file.save(f"uploaded_{file.filename}")
    return f"File {file.filename} uploaded successfully", 200

@app.route('/download', methods=['GET'])
def download_image():
    
    try:
        return send_from_directory('.', 'uploaded_image.png')
    except FileNotFoundError:
        return "File not found", 404
    


@app.route('/get-log', methods=['GET'])
def get_log():
    # return the entirety of sensor_data.json
    with open('sensor_data.json', 'r') as file:
        data = json.load(file)

    return jsonify(data)

@app.route('/clear-log', methods=['DELETE'])
def clear_log():
    # clear the contents of sensor_data.json
    with open('sensor_data.json', 'w') as file:
        json.dump({}, file)

    return "Log cleared"


if __name__ == '__main__':
    app.run(debug=True)