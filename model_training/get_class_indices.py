import os
import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Path to train directory
train_dir = '../dataset_split/train'

# Create a dummy generator to get class indices
train_datagen = ImageDataGenerator(rescale=1./255)
train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Get class indices
class_indices = train_data.class_indices

# Save to file
with open('../backend/data/class_indices.json', 'w') as f:
    json.dump(class_indices, f)

print("Class indices saved to ../backend/data/class_indices.json")
print(class_indices)
