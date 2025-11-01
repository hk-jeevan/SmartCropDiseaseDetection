from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from predict import predict_disease

app = Flask(__name__)
CORS(app)  # allows frontend (React) to connect

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "🌱 Smart Crop Disease Detection Backend Running!"

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        predicted_class, confidence = predict_disease(file_path)
        return jsonify({
            "prediction": predicted_class,
            "confidence": round(confidence * 100, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(file_path)

if __name__ == "__main__":
    app.run(debug=True)
