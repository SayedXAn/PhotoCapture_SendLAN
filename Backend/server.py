from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'received_photos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return "No photo uploaded", 400

    photo = request.files['photo']
    filepath = os.path.join(UPLOAD_FOLDER, photo.filename)
    photo.save(filepath)
    print(f"Saved photo to {filepath}")
    return "Photo received successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
