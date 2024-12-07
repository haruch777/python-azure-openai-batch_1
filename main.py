from config import AzureConfig
from csv_handler import read_meeting_minutes, prepare_batch_jsonl
from batch_processor import BatchProcessor
from result_handler import ResultHandler

def main():
    # Initialize configuration
    config = AzureConfig()
    
    # Read meeting minutes from CSV
    print("Reading meeting minutes from CSV...")
    minutes_data = read_meeting_minutes('meeting_minutes.csv')
    if not minutes_data:
        print("No data found in CSV file")
        return

    # Prepare JSONL file for batch processing
    print("Preparing batch input file...")
    input_file = "batch_input.jsonl"
    if not prepare_batch_jsonl(minutes_data, input_file):
        print("Failed to prepare batch input file")
        return

    # Initialize batch processor
    processor = BatchProcessor(config)
    
    # Submit batch job
    print("Submitting batch job...")
    batch_id = processor.submit_batch(input_file)
    if not batch_id:
        print("Failed to submit batch job")
        return

    print(f"Batch job submitted successfully. Batch ID: {batch_id}")
    
    # Wait for completion and get final status
    print("Waiting for batch job completion...")
    final_status = processor.wait_for_completion(batch_id)
    
    # Handle results
    ResultHandler.print_batch_status(final_status)
    output_file = ResultHandler.save_results(final_status)
    print(f"\nResults have been saved to '{output_file}'")

if __name__ == "__main__":
    main()