import io
from dotenv import load_dotenv
import os
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

load_dotenv(dotenv_path='..\\Data\\.env')

DREAMSTUDIO = os.getenv('DREAMSTUDIO_API')

def generate_image(text):
    stability_api = client.StabilityInference(
        key=DREAMSTUDIO,
        verbose=True,
    )

    # the object returned is a python generator
    answers = stabili