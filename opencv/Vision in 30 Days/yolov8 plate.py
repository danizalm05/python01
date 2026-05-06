 
'''
       Automatic number plate recognition with Python, Yolov8 and EasyOCR  
https://www.youtube.com/watch?v=fyJB1t0o0ms
https://github.com/computervisioneng/automatic-number-plate-recognition-python-


Train Yolov8 object detection on a custom dataset   Step by step guide 

https://www.youtube.com/watch?v=m9fH9OWn8YM

https://youtu.be/m9fH9OWn8YM?t=310

'''
'''
במקום להוריד ידנית — משתמשים בכלי הרשמי:

🛠️ OIDv6 Toolkit
pip install oidv6
הורדת dataset קטן (20 תמונות אלפקה)
oidv6 downloader --classes Alpaca --type_data train --limit 20
 output :
     int the directort where run the 'oidv6' you will  get
      OIDv6/
       └── train/
             └── Alpaca/
             ├── img1.jpg
             ├── img2.jpg
           └── ...
'''

import cv2
import torch

import pandas as pd
import requests
import os

os.makedirs("alpaca_dataset", exist_ok=True)

# --- שלב 1: מציאת Alpaca ---
classes = pd.read_csv(
    "https://storage.googleapis.com/openimages/v6/oidv6-class-descriptions.csv",
    header=None,
    names=["LabelName", "ClassName"]
)

alpaca_id = classes[classes["ClassName"].str.lower() == "alpaca"].iloc[0]["LabelName"]
print("Alpaca ID:", alpaca_id)

# --- שלב 2: טוען רק חלק קטן (קריטי!) ---
print("Loading annotations (partial)...")

df = pd.read_csv(
    "https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv",
    nrows=500000   # רק חצי מיליון שורות
)

alpaca_df = df[df["LabelName"] == alpaca_id]

image_ids = alpaca_df["ImageID"].unique()
print("Images found:", len(image_ids))

# --- שלב 3: הורדה עם fallback ל-validation ---
downloaded = 0

for img_id in image_ids:
    if downloaded >= 20:
        break

    urls = [
        f"https://storage.googleapis.com/openimages/v6/train/{img_id}.jpg",
        f"https://storage.googleapis.com/openimages/v6/validation/{img_id}.jpg"
    ]

    for url in urls:
        try:
            r = requests.get(url, timeout=5)

            if r.status_code == 200 and len(r.content) > 5000:
                path = f"alpaca_dataset/{img_id}.jpg"
                with open(path, "wb") as f:
                    f.write(r.content)

                downloaded += 1
                print(f"Downloaded {downloaded}: {img_id}")
                break

        except Exception as e:
            print("Error:", e)

print("DONE. Total downloaded:", downloaded) 