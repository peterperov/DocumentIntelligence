import configparser
import os

import matplotlib.pyplot as plt
import numpy as np
import requests
from matplotlib.patches import Polygon

import cv2
import imutils
import time

from dotenv import dotenv_values



# Define target image
# target_image_path = os.path.join("..", "images", "040603", "P6040011.jpg")
target_image_path = "SamplePictures/GreekLicenseplate.jpg"

config = dotenv_values(".env")

# CUSTOM_VISION_API_KEY
custom_vision_key = config.get("CUSTOM_VISION_API_KEY", None)
custom_vision_url = config.get("CUSTOM_VISION_URL", None)


# COMPUTER_VISION_URL 
computer_vision_key = config.get("COMPUTER_VISION_API_KEY", None)
computer_vision_url = config.get("COMPUTER_VISION_URL", None)

# Load an color (1) image in grayscale (0)
img = cv2.imread(target_image_path, 1)

# Convert image to byte string
img_str = cv2.imencode(".jpg", img)[1].tostring()

# Perform object detection using the custom vision service
custom_vision_response = requests.post(
    url=custom_vision_url, 
    data=img_str, 
    headers={
    "Content-Type": "application/octet-stream",
    "Prediction-Key": custom_vision_key,
    }
).json()

# Find bounding box with the highest confidence level
best_custom_vision_prediction = max(
    custom_vision_response["predictions"], key=lambda x: x["probability"]
)

# Extract the bounding box
bounding_box = best_custom_vision_prediction["boundingBox"]

# Define vertical distance from the left border
x = np.int32(bounding_box["left"] * img.shape[1])

# Define horizontal distance from the top border
y = np.int32(bounding_box["top"] * img.shape[0])

# Define rectangle width
w = np.int32(bounding_box["width"] * img.shape[1])

# Define rectangle height
h = np.int32(bounding_box["height"] * img.shape[0])

# Define top left point
point_one = (x, y)

# Define bottom right point
point_two = (x + w, y + h)

# Plot bounding box on image
img_box = cv2.rectangle(img, point_one, point_two, color=(0, 255, 0), thickness=2)

# Display image
plt.imshow(img_box)
plt.show()

# Crop image
img_crop = img[point_one[1] : point_two[1], point_one[0] : point_two[0]]

# Resize image if width less than 500 pixels
if img_crop.shape[1] < 500:
    img_resize = imutils.resize(img_crop, width=500)

# Display cropped image
plt.imshow(img_resize)
plt.show()

# ##########################################
# PERFORM OCR
# ############################################

# Convert cropped image to byte string
img_str = cv2.imencode(".jpg", img_resize)[1].tostring()

# save image file to disk
out_file = "temp_image.jpg"
if os.path.exists(out_file):
    os.remove(out_file)

cv2.imwrite(out_file, img_resize)

# ###################################

analyze_url = computer_vision_url + "vision/v3.0/read/analyze"

image_data = open(out_file, "rb").read()
# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': computer_vision_key, 'Content-Type': 'application/octet-stream'}

# Call Read API to perform OCR
response = requests.post(
    url=analyze_url,
    data=image_data,
    headers={
        "Ocp-Apim-Subscription-Key": computer_vision_key,
        "Content-Type": "application/octet-stream",
    },
)

time.sleep(3)

# Call Read API to get result
response_final = requests.get(
    response.headers["Operation-Location"],
    headers={"Ocp-Apim-Subscription-Key": computer_vision_key},
)

response_final.raise_for_status()

result = response_final.json()

print(result)

# Find text identified by the API
for line in result["analyzeResult"]["readResults"][0]["lines"]:
    print("Recognised text:", line["text"])

    


