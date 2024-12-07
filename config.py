from typing import Optional
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

class AzureConfig:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("AZURE_OPENAI_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def get_client(self) -> AzureOpenAI:
        """Create and return an Azure OpenAI client."""
        return AzureOpenAI(
            api_key=self.api_key,
            api_version="2023-05-15",
            azure_endpoint=self.endpoint
        )