import os
import shutil
from PIL import Image
from tqdm import tqdm

# === CONFIGURATION ===
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))  # Assuming script runs from Preprocessing
SOURCE_FOLDER = os.path.join(BASE_DIR, "data", "images")    
DEST_FOLDER = os.path.join(BASE_DIR, "Preprocessed_data", "images")  
IMAGE_SIZE = 224  # BLIP base model size

# Path to captions.json
CAPTIONS_JSON_SOURCE = os.path.join(BASE_DIR, "data", "captions.json")  
CAPTIONS_JSON_DEST = os.path.join(BASE_DIR, "Preprocessed_data", "captions.json")

# === CREATE DESTINATION FOLDER IF IT DOESN'T EXIST ===
os.makedirs(DEST_FOLDER, exist_ok=True)

# === FUNCTION TO RESIZE AND SAVE IMAGE ===
def resize_and_save_image(image_path, dest_folder):
    try:
        img = Image.open(image_path).convert('RGB')
        img_resized = img.resize((IMAGE_SIZE, IMAGE_SIZE))

        filename = os.path.basename(image_path)
        save_path = os.path.join(dest_folder, filename)

        img_resized.save(save_path)

    except Exception as e:
        print(f"Failed to process {image_path}: {e}")

# === PROCESS ALL IMAGES ===
valid_extensions = ['.jpg', '.jpeg', '.png']
image_files = [f for f in os.listdir(SOURCE_FOLDER) if os.path.splitext(f)[1].lower() in valid_extensions]

print(f"🔍 Found {len(image_files)} images to resize...")

for img_file in tqdm(image_files):
    img_path = os.path.join(SOURCE_FOLDER, img_file)
    resize_and_save_image(img_path, DEST_FOLDER)

print(f"\n✅ Resized images stored in: {DEST_FOLDER}")

# === COPY captions.json FILE ===
try:
    shutil.copy2(CAPTIONS_JSON_SOURCE, CAPTIONS_JSON_DEST)
    print(f"✅ captions.json copied to {CAPTIONS_JSON_DEST}")
except Exception as e:
    print(f"❌ Failed to copy captions.json: {e}")
