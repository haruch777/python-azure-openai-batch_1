import time
from typing import Dict, Optional
from openai import AzureOpenAI
from config import AzureConfig

class BatchProcessor:
    def __init__(self, config: AzureConfig):
        self.client = config.get_client()
        self.deployment_name = config.deployment_name

    def submit_batch(self, input_file: str) -> Optional[str]:
        """Submit a batch processing job."""
        try:
            # Upload the JSONL file
            with open(input_file, 'rb') as f:
                file_upload = self.client.files.create(
                    file=f,
                    purpose='batch'
                )

            # Submit batch job
            batch_response = self.client.batches.create(
                input_file_id=file_upload.id,
                endpoint="/chat/completions",
                completion_window="24h",
            )
            
            return batch_response.id
        except Exception as e:
            print(f"Error submitting batch job: {e}")
            return None

    def get_batch_status(self, batch_id: str) -> Dict:
        """Get the status of a batch job."""
        try:
            return self.client.batches.retrieve(batch_id).model_dump()
        except Exception as e:
            print(f"Error retrieving batch status: {e}")
            return {"status": "error", "error": str(e)}

    def wait_for_completion(self, batch_id: str, check_interval: int = 60) -> Dict:
        """Wait for batch job completion and return final status."""
        while True:
            status = self.get_batch_status(batch_id)
            
            if status.get("status") in ["succeeded", "failed", "cancelled"]:
                return status
            
            print(f"Batch job status: {status.get('status')} - Waiting {check_interval} seconds...")
            time.sleep(check_interval)