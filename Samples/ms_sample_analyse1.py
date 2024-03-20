

import requests
# If you are using a Jupyter Notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO
import time


from dotenv import dotenv_values


config = dotenv_values(".env")
subscription_key = config.get("COMPUTER_VISION_API_KEY", None)
endpoint = config.get("COMPUTER_VISION_URL", None)

# ocr_url = endpoint + "vision/v3.1/ocr"



# Set image_url to the URL of an image that you want to analyze.
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
# params = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}
# response = requests.post(analyze_url, headers=headers, params=params, json=data)

image_path = "SamplePictures/GreekLicenseplate.jpg"
image_data = open(image_path, "rb").read()
# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}

analyze_url = endpoint + "vision/v3.0/read/analyze"

# Call Read API to perform OCR
response = requests.post(
    url=analyze_url,
    data=image_data,
    headers={
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/octet-stream",
    },
)

time.sleep(3)

# Call Read API to get result
response_final = requests.get(
    response.headers["Operation-Location"],
    headers={"Ocp-Apim-Subscription-Key": subscription_key},
)

response_final.raise_for_status()

result = response_final.json()

print(result)

