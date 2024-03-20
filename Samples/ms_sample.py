import os
import sys
import requests
# If you are using a Jupyter Notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

from dotenv import dotenv_values


config = dotenv_values(".env")
subscription_key = config.get("COMPUTER_VISION_API_KEY", None)
endpoint = config.get("COMPUTER_VISION_URL", None)

ocr_url = endpoint + "vision/v3.1/ocr"

image_path = "temp_image.jpg"
# image_path = "SamplePictures/Atomist_quote_from_Democritus.png"
image_path = "SamplePictures/GreekLicensePlate.png"
# Read the image into a byte array
image_data = open(image_path, "rb").read()
# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'unk', 'detectOrientation': 'true'}
# put the byte array into your post request
response = requests.post(ocr_url, headers=headers, params=params, data = image_data)


response.raise_for_status()

analysis = response.json()

# Extract the word bounding boxes and text.
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
word_infos

print(word_infos)

# Display the image and overlay it with the extracted text.
plt.figure(figsize=(5, 5))
# image = Image.open(BytesIO(requests.get(image_url).content))

image = Image.open(image_path)

ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3],
                      fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.show()
plt.axis("off")