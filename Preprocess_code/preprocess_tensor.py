#code to preprocess the images and store as .pt file
# rgb , normalizing, resolution
import os
from PIL import Image
import torch
from torchvision import transforms
from tqdm import tqdm

# === CONFIGURATION ===
SOURCE_FOLDER = 'path/to/your/source_images'         # e.g., './images'
DEST_FOLDER = 'path/to/save/preprocessed_tensors'    # e.g., './blip_processed_tensors'
IMAGE_SIZE = 224                                     # BLIP base model image size
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

# === CREATE DESTINATION FOLDER IF IT DOESN'T EXIST ===
os.makedirs(DEST_FOLDER, exist_ok=True)

# === BLIP BASE PREPROCESSING PIPELINE ===
preprocess_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),     # Resize to 224x224
    transforms.ToTensor(),                           # Converts PIL image [0-255] to tensor [0-1]
    transforms.Normalize(mean=[0.485, 0.456, 0.406], # ImageNet mean
                         std=[0.229, 0.224, 0.225])  # ImageNet std
])

# === FUNCTION TO PREPROCESS AND SAVE ===
def preprocess_and_save(image_path, dest_folder):
    try:
        # Load and convert to RGB
        img = Image.open(image_path).convert('RGB')

        # Apply BLIP preprocessing
        img_tensor = preprocess_transform(img)

        # Extract filename without extension
        filename = os.path.splitext(os.path.basename(image_path))[0]

        # Save as .pt file
        save_path = os.path.join(dest_folder, f"{filename}.pt")
        torch.save(img_tensor, save_path)

        print(f"Saved preprocessed tensor: {save_path}")

    except Exception as e:
        print(f"Failed to process {image_path}: {e}")

# === PROCESS ALL IMAGES ===
valid_extensions = ['.jpg', '.jpeg', '.png']
image_files = [f for f in os.listdir(SOURCE_FOLDER) if os.path.splitext(f)[1].lower() in valid_extensions]

print(f"🔍 Found {len(image_files)} images to process...")

for img_file in tqdm(image_files):
    img_path = os.path.join(SOURCE_FOLDER, img_file)
    preprocess_and_save(img_path, DEST_FOLDER)

print(f"\nPreprocessed tensors stored in: {DEST_FOLDER}")
