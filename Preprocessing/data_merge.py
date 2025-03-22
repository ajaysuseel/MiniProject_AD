import os
import json
import shutil

# Define root folder
IMAGE_ROOT = "MiniProject_AD"
SUBFOLDERS = ["abhiram", "pranav", "ajay"]  # Ensure these match actual folder names

# Destination folder
DATA_FOLDER = os.path.join(IMAGE_ROOT, "data")
IMAGE_DEST = os.path.join(DATA_FOLDER, "images")
CAPTIONS_FILE = os.path.join(DATA_FOLDER, "captions.json")

# Create necessary folders
os.makedirs(IMAGE_DEST, exist_ok=True)

# Initialize combined captions list
combined_captions = []

# Process each subfolder
for folder in SUBFOLDERS:
    images_folder = os.path.join(IMAGE_ROOT, folder, "images")
    captions_path = os.path.join(IMAGE_ROOT, folder, "captions.json")

    # Move images to combined folder
    if os.path.exists(images_folder):
        images = os.listdir(images_folder)
        if not images:
            print(f"⚠️ No images found in {images_folder}")
        for img_file in images:
            img_path = os.path.join(images_folder, img_file)
            if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
                shutil.copy(img_path, os.path.join(IMAGE_DEST, img_file))
    else:
        print(f"❌ Missing images folder: {images_folder}")

    # Merge captions.json
    if os.path.exists(captions_path):
        with open(captions_path, "r") as f:
            try:
                captions = json.load(f)
                if captions:
                    combined_captions.extend(captions)
                else:
                    print(f"⚠️ Empty captions.json in {captions_path}")
            except json.JSONDecodeError:
                print(f"❌ Error: Invalid JSON format in {captions_path}")
    else:
        print(f"❌ Missing captions.json in {folder}")

# Save combined captions.json
with open(CAPTIONS_FILE, "w") as f:
    json.dump(combined_captions, f, indent=4)

print(f"✅ Images combined in {IMAGE_DEST}")
print(f"✅ Captions merged into {CAPTIONS_FILE} ({len(combined_captions)} entries)")
