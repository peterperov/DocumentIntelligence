
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

from dotenv import dotenv_values

def run_image_ocr(file_name):
    
    # COMPUTER_VISION_URL 
    config = dotenv_values(".env")
    computer_vision_key = config.get("COMPUTER_VISION_API_KEY", None)
    computer_vision_url = config.get("COMPUTER_VISION_URL", None)

    print("run_image_ocr")



file_name = "temp_image.jpg"

run_image_ocr(file_name)
