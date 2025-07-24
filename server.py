from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# ✅ Change the directory to your desired folder
UPLOAD_FOLDER = r"C:\CUP\VISA AR Photobooth\Photos"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({"error": "No photo uploaded"}), 400

    photo = request.files['photo']

    # Count existing photos to generate a new filename
    existing_files = os.listdir(UPLOAD_FOLDER)
    photo_count = len([f for f in existing_files if f.startswith('photo_') and f.endswith('.jpg')])
    new_filename = f"photo_{photo_count + 1}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, new_filename)

    photo.save(filepath)
    print(f"Saved photo as {new_filename}")
    return jsonify({"message": f"Photo saved as {new_filename}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
