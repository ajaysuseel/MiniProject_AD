import os
import json
import cv2
import shutil
import albumentations as A

# Define paths
base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
data_dir = os.path.join(base_dir, "Preprocessed_data", "images")
augmented_dir = os.path.join(base_dir, "augmented")
augmented_images_dir = os.path.join(augmented_dir, "images")
captions_file = os.path.join(base_dir, "Preprocessed_data", "captions.json")
augmented_captions_file = os.path.join(augmented_dir, "captions.json")

# Ensure output directories exist
os.makedirs(augmented_images_dir, exist_ok=True)

# Load original captions
with open(captions_file, "r") as f:
    captions = json.load(f)

# Define individual augmentations
transforms = [
    ("rotate", A.Rotate(limit=15, p=1.0)),  
    ("crop", A.Compose([
        A.CenterCrop(height=int(0.95 * 224), width=int(0.95 * 224), p=1.0),  # Crop 95% of the image
        A.Resize(* (224, 224), p=1.0)  # Resize back to 224x224
    ])),
    ("color", A.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1, p=1.0)),  
    ("noise", A.GaussNoise(var_limit=(0.1, 0.2), p=1.0))  
]

# Store new captions
new_captions = []
total_images = 0

for entry in captions:
    filename = entry["filename"]
    description = entry["description"]
    file_path = os.path.join(data_dir, filename)

    if not os.path.exists(file_path):
        continue

    # Copy original image
    original_dest = os.path.join(augmented_images_dir, filename)
    shutil.copy(file_path, original_dest)
    new_captions.append({"filename": filename, "description": description})  
    total_images += 1  # Count original image

    # Read image
    image = cv2.imread(file_path)
    if image is None:
        continue
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply each transformation separately
    for transform_name, transform in transforms:
        augmented = transform(image=image)["image"]

        # Generate new filename for augmented image
        file_base, ext = os.path.splitext(filename)
        new_filename = f"{file_base}_{transform_name}{ext}"
        new_file_path = os.path.join(augmented_images_dir, new_filename)

        # Save the augmented image
        cv2.imwrite(new_file_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))

        # Add correct caption for augmented image
        new_captions.append({"filename": new_filename, "description": description})
        total_images += 1  # Count each augmented image

# Save updated captions
with open(augmented_captions_file, "w") as f:
    json.dump(new_captions, f, indent=4)

print(f"✅ Augmentation complete! Captions are correctly mapped to images.")
print(f"📸 Total images processed (original + augmented): {total_images}")
