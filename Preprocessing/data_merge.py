import os
import json
import shutil

# Set paths relative to Preprocessing/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Go up to MiniProject_AD
IMAGE_ROOT = os.path.join(BASE_DIR, "raw_data")  # Source: raw_data
DATA_FOLDER = os.path.join(BASE_DIR, "data")  # Destination: data

SUBFOLDERS = ["kishan","abhiram_new", "pranav", "ajay","abhiram"]
IMAGE_DEST = os.path.join(DATA_FOLDER, "images")
CAPTIONS_FILE = os.path.join(DATA_FOLDER, "captions.json")

# Create necessary folders
os.makedirs(IMAGE_DEST, exist_ok=True)

# Initialize combined captions list and counters
total_images_added = 0
total_images_skipped = 0
combined_captions = []

# Process each subfolder
for folder in SUBFOLDERS:
    images_folder = os.path.join(IMAGE_ROOT, folder, "images")
    captions_path = os.path.join(IMAGE_ROOT, folder, "captions.json")
    
    print(f"🔍 Checking {images_folder}...")
    
    if not os.path.exists(images_folder):
        print(f"❌ Missing images folder: {images_folder}")
        continue
    
    if not os.path.exists(captions_path):
        print(f"❌ Missing captions.json in {captions_path}")
        continue
    
    # Load captions
    try:
        with open(captions_path, "r") as f:
            captions = json.load(f)
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in {captions_path}")
        continue
    
    # Convert captions list into a dictionary for quick lookup
    caption_dict = {entry["filename"]: entry["description"] for entry in captions}
    
    images = os.listdir(images_folder)
    
    for img_file in images:
        if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
            if img_file in caption_dict:
                # Copy image if caption exists
                shutil.copy(os.path.join(images_folder, img_file), os.path.join(IMAGE_DEST, img_file))
                combined_captions.append({"filename": img_file, "description": caption_dict[img_file]})
                total_images_added += 1
            else:
                print(f"⚠️ No caption found for {img_file}, skipping...")
                total_images_skipped += 1

# Save combined captions.json
with open(CAPTIONS_FILE, "w") as f:
    json.dump(combined_captions, f, indent=4)

# Summary
print(f"✅ Total images added to {IMAGE_DEST}: {total_images_added}")
#print(f"⚠️ Total images skipped due to missing captions: {total_images_skipped}")
print(f"✅ Captions merged into {CAPTIONS_FILE} ({len(combined_captions)} entries)")
