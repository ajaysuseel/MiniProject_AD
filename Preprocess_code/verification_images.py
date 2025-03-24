#to check if the images have been processed correctly
import os
from PIL import Image
from tqdm import tqdm

DEST_FOLDER = '/home/abhiram/Documents/MiniProject_AD/Preprocessed_data/images'
EXPECTED_SIZE = (224, 224)

def verify_images(folder):
    invalid_images = []
    image_files = [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg', '.png']]
    
    print(f"🔍 Checking {len(image_files)} images in {folder}...")
    
    for img_file in tqdm(image_files, desc="Verifying images"):
        img_path = os.path.join(folder, img_file)
        try:
            with Image.open(img_path) as img:
                # Check size
                if img.size != EXPECTED_SIZE:
                    print(f"Size mismatch in {img_file}: {img.size}")
                    invalid_images.append(img_file)
        except Exception as e:
            print(f"Cannot open {img_file}: {e}")
            invalid_images.append(img_file)

    if invalid_images:
        print(f"\nFound {len(invalid_images)} problematic images:")
        for f in invalid_images:
            print(f" - {f}")
    else:
        print("\nAll images verified successfully!")

# Run verification
verify_images(DEST_FOLDER)
