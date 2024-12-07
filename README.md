# Meeting Minutes Analyzer

This program analyzes meeting minutes using Azure OpenAI's Batch API to predict demand for data management consulting services.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure Azure OpenAI credentials:
Create a `.env` file and set the following environment variables:
```
AZURE_OPENAI_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_DEPLOYMENT=your_deployment_name_here
```

3. Prepare your data:
Create a CSV file named `meeting_minutes.csv` with your meeting minutes data.

## Usage

Run the program:
```bash
python main.py
```

The program will:
1. Read meeting minutes from the CSV file
2. Create a JSONL file for batch processing
3. Submit a batch job to Azure OpenAI
4. Monitor the job status until completion
5. Save detailed results to a JSON file

## Process Flow

1. CSV data is read and converted to the required format
2. A JSONL file is created with the proper structure for batch processing
3. The JSONL file is uploaded to Azure OpenAI
4. A batch job is submitted and monitored
5. Results are saved once the job completes