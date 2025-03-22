# MiniProject_AD
Vision language model for detecting out of label hazards in autonomous driving

MiniProject_AD/  
│── raw_data/                   # 📂 Source data (images & captions)  
│   ├── kishan/  
│   │   ├── images/             # 🖼️ Images for Kishan  
│   │   ├── captions.json       # 📝 Captions for Kishan's images  
│   ├── abhiram/  
│   │   ├── images/  
│   │   ├── captions.json  
│   ├── abhiram_new/  
│   │   ├── images/  
│   │   ├── captions.json  
│   ├── pranav/  
│   │   ├── images/  
│   │   ├── captions.json  
│   ├── ajay/  
│   │   ├── images/  
│   │   ├── captions.json  
│  
│── data/                        # 📂 Processed dataset (after merging)  
│   ├── images/                  # 🖼️ All merged images from raw_data  
│   ├── captions.json             # 📝 Merged captions.json for all images  
│  
│── Preprocessing/                # 🔄 Data preprocessing scripts  
│   ├── data_merge.py             # 📝 Script to merge images & captions  
│   ├── other_preprocessing.py    # 📝 Additional preprocessing (optional)  
│  
│── Finetuning/                   # 🤖 Fine-tuning scripts & models  
│   ├── finetune_blip.py          # 📝 BLIP fine-tuning script  
│   ├── model_weights/            # 💾 Fine-tuned model checkpoints  
│   ├── logs/                     # 📊 Training logs & metrics  
│  
│── Hazard_detection/             # 🚨 Hazard detection module  
│   ├── detect_hazard.py          # 📝 Hazard detection model script  
│   ├── test_videos/              # 🎥 Sample videos for testing  
│   ├── results/                  # 📊 Model output results  
│  
│── Documentation/                # 📖 Project documentation  
│   ├── project_overview.md       # 📝 Overview of the project  
│   ├── model_architecture.pdf    # 📄 Model architecture diagrams  
│   ├── references/               # 🔗 Research papers & related materials  
│  
│── README.md                     # 📜 Project description (this file)  
│── requirements.txt               # 📦 Dependencies list for setup  
│── .gitignore                     # 🚫 Ignore unnecessary files in Git  

