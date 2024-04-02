"""
This code sample shows Prebuilt ID Document operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

from dotenv import dotenv_values

import json

config = dotenv_values(".env")

# FORM_RECOGNIZER_ENDPOINT
fr_endpoint = config.get("FORM_RECOGNIZER_ENDPOINT", None)
# FORM_RECOGNIZER_KEY
fr_key = config.get("FORM_RECOGNIZER_KEY", None)

image_file = "W:/GITHUB/DocumentIntelligence/IrishDL/Ireland DL 001.png"

# W:/GITHUB/DocumentIntelligence/SamplePictures/Driving License 01.jpg
image_file = "W:/GITHUB/DocumentIntelligence/SamplePictures/Driving License 01.jpg"

# sample document
formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/DriverLicense.png"

document_analysis_client = DocumentAnalysisClient( endpoint=fr_endpoint, credential=AzureKeyCredential(fr_key) )
# poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-idDocument", formUrl)

# SDK documentation:
# https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentanalysisclient?view=azure-python
# languages support
# https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/language-support-ocr
# Greek	el


# fr_locale="en-US"
fr_locale="el"


with open(image_file, "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-idDocument", document=f, locale=fr_locale
    )
id_documents = poller.result()

print (poller.result)

for idx, id_document in enumerate(id_documents.documents):
    print(idx)
    print("---")
    
    # json_data = json.dumps(id_document, indent=4)
    # f = open('data.json', 'wb')
    # f.write(json_data)

    print("--------Recognizing ID document #{}--------".format(idx + 1))
    first_name = id_document.fields.get("FirstName")
    if first_name:
        print(
            "First Name: {} has confidence: {}".format(
                first_name.value, first_name.confidence
            )
        )
    last_name = id_document.fields.get("LastName")
    if last_name:
        print(
            "Last Name: {} has confidence: {}".format(
                last_name.value, last_name.confidence
            )
        )
    document_number = id_document.fields.get("DocumentNumber")
    if document_number:
        print(
            "Document Number: {} has confidence: {}".format(
                document_number.value, document_number.confidence
            )
        )
    dob = id_document.fields.get("DateOfBirth")
    if dob:
        print(
            "Date of Birth: {} has confidence: {}".format(dob.value, dob.confidence)
        )
    doe = id_document.fields.get("DateOfExpiration")
    if doe:
        print(
            "Date of Expiration: {} has confidence: {}".format(
                doe.value, doe.confidence
            )
        )
    sex = id_document.fields.get("Sex")
    if sex:
        print("Sex: {} has confidence: {}".format(sex.value, sex.confidence))
    address = id_document.fields.get("Address")
    if address:
        print(
            "Address: {} has confidence: {}".format(
                address.value, address.confidence
            )
        )
    country_region = id_document.fields.get("CountryRegion")
    if country_region:
        print(
            "Country/Region: {} has confidence: {}".format(
                country_region.value, country_region.confidence
            )
        )
    region = id_document.fields.get("Region")
    if region:
        print(
            "Region: {} has confidence: {}".format(region.value, region.confidence)
        )
