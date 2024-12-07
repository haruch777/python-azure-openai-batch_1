import json
from typing import List, Dict
from datetime import datetime

class ResultHandler:
    @staticmethod
    def save_results(results: Dict, output_file: str = None) -> str:
        """Save batch processing results to a JSON file."""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f'batch_results_{timestamp}.json'

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        return output_file

    @staticmethod
    def print_batch_status(status: Dict):
        """Print batch processing status."""
        print("\nBatch Processing Status:")
        print("-" * 50)
        print(f"Status: {status.get('status', 'Unknown')}")
        print(f"Created at: {status.get('created_at', 'Unknown')}")
        
        if status.get('error'):
            print(f"Error: {status['error']}")
        
        if status.get('metrics'):
            metrics = status['metrics']
            print("\nMetrics:")
            print(f"Total files: {metrics.get('total_files', 0)}")
            print(f"Completed files: {metrics.get('completed_files', 0)}")
            print(f"Failed files: {metrics.get('failed_files', 0)}")
            
        print("-" * 50)