import torch
import os
from tqdm import tqdm

DEST_FOLDER = '/home/abhiram/Pictures/drive1/processed_tensors'
EXPECTED_SHAPE = (3, 224, 224)

def verify_tensors(folder):
    invalid_files = []
    tensor_files = [f for f in os.listdir(folder) if f.endswith('.pt')]

    print(f"🔍 Verifying {len(tensor_files)} tensor files...")

    for t_file in tqdm(tensor_files):
        path = os.path.join(folder, t_file)
        try:
            tensor = torch.load(path)
            if tensor.shape != EXPECTED_SHAPE:
                print(f"Shape mismatch in {t_file}: {tensor.shape}")
                invalid_files.append(t_file)
        except Exception as e:
            print(f"Failed to load {t_file}: {e}")
            invalid_files.append(t_file)

    if invalid_files:
        print(f"\nFound {len(invalid_files)} problematic files:")
        for f in invalid_files:
            print(f" - {f}")
    else:
        print("\nAll tensors verified successfully!")

# Run it
verify_tensors(DEST_FOLDER)
