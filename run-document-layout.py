"""
This code sample shows Prebuilt Read operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

from dotenv import dotenv_values
import matplotlib.pyplot as plt
import numpy as np
import cv2

import json

config = dotenv_values(".env")

# FORM_RECOGNIZER_ENDPOINT
endpoint = config.get("FORM_RECOGNIZER_ENDPOINT", None)
# FORM_RECOGNIZER_KEY
key = config.get("FORM_RECOGNIZER_KEY", None)

print( "**********************************************")
print( "ENDPOINT:")
print(endpoint)
print( "**********************************************")


image_file = "S:/OneDrive - CaptainAzure/DEMOS/Greek - Copy.PNG"

def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])

def analyze_read():
    # sample document
    document_analysis_client = DocumentAnalysisClient( endpoint=endpoint, credential=AzureKeyCredential(key) )

    with open(image_file, "rb") as f:
        poller = document_analysis_client.begin_analyze_document(
            "prebuilt-read", document=f
            # , locale=fr_locale
        )    
    
    # poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-read", formUrl)
    result = poller.result()

    print ("Document contains content: ", result.content)
    
    for idx, style in enumerate(result.styles):
        print(
            "Document contains {} content".format(
                "handwritten" if style.is_handwritten else "no handwritten"
            )
        )

    for page in result.pages:
        print("----Analyzing Read from page #{}----".format(page.page_number))
        print(
            "Page has width: {} and height: {}, measured with unit: {}".format(
                page.width, page.height, page.unit
            )
        )

        for line_idx, line in enumerate(page.lines):
            print(
                "...Line # {} has text content '{}' within bounding box '{}'".format(
                    line_idx,
                    line.content,
                    format_bounding_box(line.polygon),
                )
            )

        for word in page.words:
            print(
                "...Word '{}' has a confidence of {}".format(
                    word.content, word.confidence
                )
            )

    print("----------------------------------------")
    print("Confidence")
    print("----------------------------------------")

    confidence_threshold = 0.7

    # Define top left point
    # point_one = (x, y)
    # Define bottom right point
    # point_two = (x + w, y + h)
    # Plot bounding box on image
    # img_box = cv2.rectangle(img, point_one, point_two, color=(0, 255, 0), thickness=2)

    img = cv2.imread(image_file, 1)
    img_box = img



    for page in result.pages:
        for word in page.words: 
            if word.confidence < confidence_threshold:
                # {} {} {} {} {} {}
                # print("{} | {} {} {} {} | {}".format(word.confidence, word.polygon[0], word.polygon[1], word.polygon[2], word.polygon[3], word.content))
                print("{} | {}".format(word.confidence, word.content))
                
                x1 = np.int32(word.polygon[0].x)
                y1 = np.int32(word.polygon[0].y)

                x2 = np.int32(word.polygon[2].x)
                y2 = np.int32(word.polygon[2].y)

                point_one = (x1,y1)
                point_two = (x2, y2)

                img_box = cv2.rectangle(img_box, point_one, point_two, color=(0, 255, 0), thickness=2)


    plt.imshow(img_box)
    plt.show()



if __name__ == "__main__":
    analyze_read()
