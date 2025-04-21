In this step, we created an automated pipeline that listens for new files in Google Cloud Storage (GCS), flattens Alpha Vantage JSON data, and loads it into BigQuery. This enables real-time analytics on structured stock data.

# Goal

- Detect new JSON files in GOOGLE Cloud Storage
- Flatten the nested Alpha Vantage time series data.
- Store the flattened data as newline-delimited JSON.
- Automatically load it into BigQuery.


## Architect Overview
`GCS Bucket (raw) → Cloud Function → GCS Bucket (flat) → BigQuery Table`

Trigger: New .json file uploaded to AAPL/, MSFT/, etc.
Processing: Cloud Function flattens it
Destination: Writes to AAPL_flat/ and loads to stock_data.aapl_flat


## Create a folder

(example : flatten and load)
- Add main.py and requirements.txt to it.

  **Cloud Function Code** (main.py):
    - Extracts symbol from folder path
    - Parses Alpha Vantage JSON
    - Converts to rows (timestamp, open, high, low, close, volume)
    - Uploads flattened NDJSON to GCS
    - Loads NDJSON into BigQuery with autodetected schema
      (Includes check to skip empty files)


## Deployment

(run this command from within the flatten-and-load/ folder)

`gcloud functions deploy flatten_and_load_to_bigquery \` \
 ` --runtime python310 \` \
  `--trigger-resource stock-raw-data-stock-market-analytics-457419 \` \
 ` --trigger-event google.storage.object.finalize \` \
  `--entry-point main \` \
 ` --source . \` \
  `--region us-central1 `

## Testing the function

1. Run the scheduler to fetch new stock data:
   
   `gcloud scheduler jobs run trigger-stock-fetch --location=us-central1`

2. Check if flat files appear:
   
   `gsutil ls gs://stock-raw-data-stock-market-analytics-457419/MSFT_flat/`

3. Confirm BigQuery tables:
   
   `bq ls stock_data`

## Outcome
By the end of this step, data pipeline supports fully serverless real-time ingestion into BigQuery, ready for querying and analysis.
