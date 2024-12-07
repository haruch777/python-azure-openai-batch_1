from typing import List, Dict
from openai import AzureOpenAI
from config import AzureConfig

class AzureOpenAIClient:
    def __init__(self, config: AzureConfig):
        self.client = config.get_client()
        self.deployment_name = config.deployment_name

    def analyze_minutes(self, minutes_list: List[str]) -> List[Dict]:
        """Analyze meeting minutes using Azure OpenAI API."""
        results = []
        
        for minute in minutes_list:
            try:
                response = self.client.chat.completions.create(
                    model=self.deployment_name,
                    messages=[
                        {"role": "system", "content": "You are an AI trained to analyze meeting minutes and determine if there is a demand for data management consulting. Respond with only 'Yes' or 'No'."},
                        {"role": "user", "content": f"Based on these meeting minutes, is there a demand for data management consulting? Minutes: {minute}"}
                    ],
                    temperature=0,
                    max_tokens=3
                )
                
                prediction = response.choices[0].message.content.strip()
                results.append({
                    "minutes": minute,
                    "has_demand": prediction
                })
            except Exception as e:
                print(f"Error in API request: {e}")
                results.append({
                    "minutes": minute,
                    "has_demand": "Error"
                })
        
        return results