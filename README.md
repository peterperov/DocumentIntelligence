


# Prereqs

## train images

http://www.zemris.fer.hr/projects/LicensePlates/english/baza_slika.zip


## pip installs

pip install -r requirements. txt

https://pypi.org/project/azure-ai-formrecognizer/


```
    pip install azure-ai-formrecognizer

    pip install matplotlib

    pip install opencv-python


    pip install imutils

```

# .env file

.env file needs to be placed at this folder with the following key/value pairs defined. 

```

FORM_RECOGNIZER_ENDPOINT = "https://eastus.api.cognitive.microsoft.com/"
FORM_RECOGNIZER_KEY = ""

CUSTOM_VISION_API_KEY = ""
CUSTOM_VISION_API_KEY = ""

COMPUTER_VISION_URL = ""
COMPUTER_VISION_API_KEY = ""

 
```


# Microsoft Document Intelligence sample code: 
 
Samples with detailed explanation:
 
https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-formrecognizer/3.2.0b1/index.html#using-the-general-document-model



# Codez

```
document_analysis_client.begin_analyze_document

```

https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentanalysisclient?view=azure-python#azure-ai-formrecognizer-documentanalysisclient-begin-analyze-document

```

```
