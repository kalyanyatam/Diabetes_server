from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read()))  # Convert to PIL Image
    text = pytesseract.image_to_string(image)  # Extract text

    return jsonify({"text": text})  # Send extracted text

if __name__ == "__main__":
    app.run(debug=True)  # Ensure it's running on port 5000
