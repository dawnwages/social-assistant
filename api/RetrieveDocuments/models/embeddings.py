import requests
import json
import os
from azure.ai.inference import EmbeddingsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()
AZURE_API_KEY = os.getenv("AZURE_TOKEN")

def generate_embedding(text):
    azure_endpoint = "https://models.inference.ai.azure.com"
    model_name = "text-embedding-3-small"

    client = EmbeddingsClient(
        endpoint=azure_endpoint,
        credential=AzureKeyCredential(AZURE_API_KEY)
    )

    response = client.embed(input=text, model=model_name)
    embeddings = [item.embedding for item in response.data]

    if response.status_code == 200:
        return embeddings
    else:
        raise Exception(f"Error from Azure AI Inference: {response.status_code} {response.text}")
