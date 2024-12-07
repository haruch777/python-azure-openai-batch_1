import pandas as pd
from typing import List, Dict

def read_meeting_minutes(file_path: str) -> List[Dict[str, str]]:
    """Read meeting minutes from CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def prepare_batch_jsonl(minutes_data: List[Dict[str, str]], output_path: str) -> bool:
    """Prepare JSONL file for batch processing."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for row in minutes_data:
                messages = [
                    {"role": "system", "content": "You are an AI trained to analyze meeting minutes and determine if there is a demand for data management consulting. Respond with only 'Yes' or 'No'."},
                    {"role": "user", "content": f"Based on these meeting minutes, is there a demand for data management consulting? Minutes: {row['minutes']}"}
                ]
                batch_item = {
                    "messages": messages,
                    "temperature": 0,
                    "max_tokens": 3
                }
                f.write(f"{pd.io.json.dumps(batch_item)}\n")
        return True
    except Exception as e:
        print(f"Error preparing JSONL file: {e}")
        return False