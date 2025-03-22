import json
import random

# Path to your original captions JSON file
INPUT_JSON_PATH = "./pranav/captions.json"
OUTPUT_JSON_PATH = "./pranav/contrastive_captions.json"

# Load the original dataset
with open(INPUT_JSON_PATH, "r") as f:
    data = json.load(f)

print(f"Loaded {len(data)} entries from {INPUT_JSON_PATH}.")

# Extract all positive captions from the dataset
positive_captions = [item["description"] for item in data]

# Generate new contrastive dataset
contrastive_data = []
for i, item in enumerate(data):
    pos_caption = item["description"]
    # Pick a random negative caption that is different from the positive caption
    neg_caption = random.choice(positive_captions)
    while neg_caption == pos_caption:
        neg_caption = random.choice(positive_captions)
    
    contrastive_data.append({
        "filename": item["filename"],
        "pos_caption": pos_caption,
        "neg_caption": neg_caption
    })
    print(f"Processed {i+1}/{len(data)}: {item['filename']}")

# Save the new contrastive dataset
with open(OUTPUT_JSON_PATH, "w") as f:
    json.dump(contrastive_data, f, indent=4)

print(f"Contrastive dataset saved as {OUTPUT_JSON_PATH}.")
