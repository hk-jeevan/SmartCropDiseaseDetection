from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os

# Load the trained model
MODEL_PATH = "../backend/model/plant_disease_model.h5"
model = load_model(MODEL_PATH)

# Load class indices
CLASS_MAP_PATH = "../backend/data/class_indices.json"
with open(CLASS_MAP_PATH, "r", encoding="utf-8") as f:
    class_labels = json.load(f)

# Load disease info
DISEASE_INFO_PATH = "../backend/data/disease_info.json"
with open(DISEASE_INFO_PATH, "r", encoding="utf-8") as f:
    DISEASE_INFO = json.load(f)

# Function to predict
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

        # Get label from class_indices
        label = list(class_labels.keys())[list(class_labels.values()).index(predicted_class)]
        info = DISEASE_INFO.get(label, {})

        return {
            "label": label,
            "confidence": round(confidence * 100, 2),
            "details": info
        }

    except Exception as e:
        return {
            "label": "Error",
            "confidence": 0.0,
            "details": {"error": str(e)}
        }

# Test with different images
test_images = [
    "../dataset_split/test/Apple___Apple_scab/c563cf1c-da17-4c03-b3e8-b306334e0270___FREC_Scab 2933_new30degFlipLR.JPG",
    "../dataset_split/test/Apple___Black_rot/c8269293-ae8c-4ac0-8eb3-6574683f1b2e___JR_FrgE.S 8699.JPG",
    "../dataset_split/test/Tomato___healthy/0a334ae6-bea3-4453-b200-85e082794d56___GH_HL Leaf 310.1.JPG",
    "../dataset_split/test/Potato___Early_blight/0a6983a5-895e-4e68-9edb-88adf79211e9___RS_Early.B 9072.JPG"
]

for img_path in test_images:
    if os.path.exists(img_path):
        result = predict_disease(img_path)
        print(f"\nImage: {os.path.basename(img_path)}")
        print(f"Predicted: {result['label']} ({result['confidence']}%)")
        print(f"Description: {result['details'].get('description', 'N/A')}")
    else:
        print(f"Image not found: {img_path}")
