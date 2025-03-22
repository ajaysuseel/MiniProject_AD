import os
import json
import shutil

# Define root folder (where abhiram, pranav, ajay exist)
IMAGE_ROOT = "MiniProject_AD"
SUBFOLDERS = ["abhiram", "pranav", "ajay"]

# Destination folder inside MiniProject_AD
DATA_FOLDER = os.path.join(IMAGE_ROOT, "data")
IMAGE_DEST = os.path.join(DATA_FOLDER, "images")
CAPTIONS_FILE = os.path.join(DATA_FOLDER, "captions.json")

# Create necessary folders
os.makedirs(IMAGE_DEST, exist_ok=True)

# Initialize list to store combined captions
combined_captions = []

# Process each subfolder
for folder in SUBFOLDERS:
    images_folder = os.path.join(IMAGE_ROOT, folder, "images")  # Images inside subfolder
    captions_path = os.path.join(IMAGE_ROOT, folder, "captions.json")

    # Move images to combined folder
    if os.path.exists(images_folder):
        for img_file in os.listdir(images_folder):
            img_path = os.path.join(images_folder, img_file)
            if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
                shutil.copy(img_path, os.path.join(IMAGE_DEST, img_file))

    # Merge captions.json
    if os.path.exists(captions_path):
        with open(captions_path, "r") as f:
            captions = json.load(f)
            combined_captions.extend(captions)  # Append captions list

# Save combined captions.json
with open(CAPTIONS_FILE, "w") as f:
    json.dump(combined_captions, f, indent=4)

print(f"✅ Images combined in {IMAGE_DEST}")
print(f"✅ Captions merged into {CAPTIONS_FILE}")
