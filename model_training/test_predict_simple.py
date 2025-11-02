from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os

# Path to model
model_path = "../backend/model/plant_disease_model.h5"
model = load_model(model_path)

# Path to test image
img_path = "../dataset_split/test/Apple___Apple_scab/c563cf1c-da17-4c03-b3e8-b306334e0270___FREC_Scab 2933_new30degFlipLR.JPG"

# Load and preprocess image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Predict
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)[0]

print("Predicted Class Index:", predicted_class)

# Load disease info
DISEASE_INFO_PATH = "../backend/data/disease_info.json"
with open(DISEASE_INFO_PATH, "r", encoding="utf-8") as f:
    DISEASE_INFO = json.load(f)

class_labels = list(DISEASE_INFO.keys())

if predicted_class < len(class_labels):
    label = class_labels[predicted_class]
    print("Predicted Label:", label)
    info = DISEASE_INFO.get(label, {})
    print("Description:", info.get("description", "No description"))
    print("Solution:", info.get("solution", "No solution"))
else:
    print("Predicted class index out of range")
