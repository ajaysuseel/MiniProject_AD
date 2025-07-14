# MiniProject_AD
Vision language model for detecting out of label hazards in autonomous driving

Basically we generate captions for driving scene images using finetuned BLIP and use these captions as input to GNN for detecting hazard severity.

Development
-->Finetune BLIP using DHPR dataset with custom captions
-->Train GNN on caption-rating pairs
-->Evaluate full pipeline

To run
    Open "Project_app_with_explainability" in Colab and after copying the models into drive and changing path accordingly,the pipeline works perfectly

Future Directions
-->Better models like BLIP2
-->Multilingual captions
-->Manually evaluate image-caption pairs and finetune to increase caption accuracy
-->Use such captions for diverse downstream tasks


Gemini_Captions
https://drive.google.com/drive/folders/1c9oY88vtBubt5dunmQm4g6LPNmn-0Njy?usp=drive_link

gemini_models
https://drive.google.com/drive/folders/1oouePirCzzAPSiJ4fUW1mm3M7c-_gDnm?usp=drive_link