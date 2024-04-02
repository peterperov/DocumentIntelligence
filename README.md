


# Prereqs

## train images

http://www.zemris.fer.hr/projects/LicensePlates/english/baza_slika.zip


## pip installs

https://pypi.org/project/azure-ai-formrecognizer/


```
    pip install azure-ai-formrecognizer

    pip install matplotlib

    pip install opencv-python


    pip install imutils

```

# .env file

```

FORM_RECOGNIZER_ENDPOINT = "https://eastus.api.cognitive.microsoft.com/"
FORM_RECOGNIZER_KEY = ""

CUSTOM_VISION_API_KEY = ""

COMPUTER_VISION_URL = ""
COMPUTER_VISION_API_KEY = ""

```



# Codez

```
document_analysis_client.begin_analyze_document

```

https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentanalysisclient?view=azure-python#azure-ai-formrecognizer-documentanalysisclient-begin-analyze-document

```

```
