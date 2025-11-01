import numpy as np
from tensorflow.keras.preprocessing import image

# Function to preprocess uploaded image
def preprocess_image(img_path):
    """
    Loads and preprocesses the image for prediction.
    """
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# Example mapping — update these later with real labels from your model
CLASS_NAMES = [
    "Apple - Healthy",
    "Apple - Scab",
    "Apple - Black Rot",
    "Corn - Healthy",
    "Corn - Gray Leaf Spot",
    "Corn - Common Rust",
    "Tomato - Healthy",
    "Tomato - Late Blight",
    "Tomato - Leaf Mold"
]

# Example solutions (you can expand this later)
SOLUTIONS = {
    "Apple - Scab": "Remove and destroy infected leaves. Use fungicide sprays like captan or mancozeb.",
    "Apple - Black Rot": "Prune infected branches and use copper-based fungicide.",
    "Corn - Gray Leaf Spot": "Rotate crops and use resistant hybrids.",
    "Corn - Common Rust": "Apply fungicides at the first sign of disease.",
    "Tomato - Late Blight": "Use certified seeds and avoid overhead irrigation.",
    "Tomato - Leaf Mold": "Increase air circulation and reduce humidity.",
    "Healthy": "Your plant is healthy! Keep monitoring regularly."
}


def get_prediction_and_solution(pred_index):
    """
    Maps predicted class index to label and gives solution.
    """
    if pred_index < len(CLASS_NAMES):
        disease_name = CLASS_NAMES[pred_index]
        solution = SOLUTIONS.get(disease_name.split(" - ")[-1], "No solution available.")
        return disease_name, solution
    else:
        return "Unknown", "No solution found."
