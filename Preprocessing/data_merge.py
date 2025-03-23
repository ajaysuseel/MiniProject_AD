import os
import json
import shutil

# Set paths relative to Preprocessing/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Go up to MiniProject_AD
IMAGE_ROOT = os.path.join(BASE_DIR, "raw_data")  # Source: raw_data
DATA_FOLDER = os.path.join(BASE_DIR, "data")  # Destination: data

SUBFOLDERS = ["abhiram_new", "pranav", "ajay"]
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

    print(f"🔍 Checking {images_folder}...")
    if os.path.exists(images_folder):
        images = os.listdir(images_folder)
        if not images:
            print(f"⚠️ No images found in {images_folder}")
        else:
            for img_file in images:
                img_path = os.path.join(images_folder, img_file)
                if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
                    shutil.copy(img_path, os.path.join(IMAGE_DEST, img_file))
    else:
        print(f"❌ Missing images folder: {images_folder}")

    print(f"🔍 Checking {captions_path}...")
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
        print(f"❌ Missing captions.json in {captions_path}")

# Save combined captions.json
with open(CAPTIONS_FILE, "w") as f:
    json.dump(combined_captions, f, indent=4)

print(f"✅ Images combined in {IMAGE_DEST}")
print(f"✅ Captions merged into {CAPTIONS_FILE} ({len(combined_captions)} entries)")
