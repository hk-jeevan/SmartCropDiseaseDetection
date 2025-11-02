import json
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

# Load the trained model
MODEL_PATH = os.path.join("model", "plant_disease_model.h5")
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully!")

# Load disease info JSON
DISEASE_INFO_PATH = os.path.join("data", "disease_info.json")
with open(DISEASE_INFO_PATH, "r", encoding="utf-8") as f:
    DISEASE_INFO = json.load(f)

# Load class indices (if exists), otherwise use keys from disease_info.json
CLASS_MAP_PATH = os.path.join("data", "class_indices.json")
if os.path.exists(CLASS_MAP_PATH):
    with open(CLASS_MAP_PATH, "r", encoding="utf-8") as f:
        class_indices_dict = json.load(f)
    # Convert dict to list: class_labels[idx] = name
    class_labels = [None] * len(class_indices_dict)
    for name, idx in class_indices_dict.items():
        class_labels[idx] = name
else:
    class_labels = list(DISEASE_INFO.keys())

num_classes_json = len(class_labels)


def predict_disease(img_path):
    try:
        # Preprocess image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Model prediction
        prediction = model.predict(img_array)
        predicted_class = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        # Safety check for class range
        if predicted_class >= num_classes_json:
            label = "Unknown"
            info = {
                "description": "Predicted class index out of range.",
                "solution": "Please retrain the model or update disease_info.json."
            }
        else:
            label = class_labels[predicted_class]
            info = DISEASE_INFO.get(label, {})

        return {
            "label": label,
            "confidence": round(confidence * 100, 2),
            "details": info
        }

    except Exception as e:
        print("❌ Error inside predict_disease:", e)
        return {
            "label": "Error",
            "confidence": 0.0,
            "details": {"error": str(e)}
        }
