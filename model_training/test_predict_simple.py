from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Path to model
model_path = "../backend/model/plant_disease_model.h5"
model = load_model(model_path)

# Path to test image
img_path = "../dataset_split/test/Apple___Apple_scab/your_image.jpg"

# Load and preprocess image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Predict
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)[0]

print("Predicted Class Index:", predicted_class)
