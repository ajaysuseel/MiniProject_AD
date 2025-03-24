# how to normalize the images - saved as image file , not .pt and use them in finetuning
from torchvision import transforms
from torch.utils.data import Dataset
from PIL import Image
import json
import os

class BlipDataset(Dataset):
    def __init__(self, json_file, image_folder, transform=None):
        with open(json_file, 'r') as f:
            self.data = json.load(f)
        
        self.image_folder = image_folder
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        image_path = os.path.join(self.image_folder, item['filename'])
        caption = item['caption']

        img = Image.open(image_path).convert('RGB')
        
        if self.transform:
            img = self.transform(img)

        return img, caption

# Transform for BLIP Base
blip_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Example dataset initialization
dataset = BlipDataset(
    json_file='your_dataset.json',
    image_folder='/home/abhiram/Pictures/drive1/images',
    transform=blip_transform
)
