from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from predict import predict_disease

app = Flask(__name__)
CORS(app)  # Allow frontend connection (React, etc.)

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
        result = predict_disease(file_path)
        # ✅ Wrap result so frontend can access as response.data.prediction
        return jsonify({"prediction": result})
    except Exception as e:
        import traceback
        print("❌ Error during prediction:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    app.run(debug=True)
