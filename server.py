from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow all origins for now

UPLOAD_FOLDER = 'received_photos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return "Server is running", 200

@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({"error": "No photo uploaded"}), 400

    photo = request.files['photo']
    filepath = os.path.join(UPLOAD_FOLDER, photo.filename)
    photo.save(filepath)
    print(f"Saved photo to {filepath}")
    return jsonify({"message": "Photo received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
