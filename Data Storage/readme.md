# Goal
- Listens to the stock-data-topic Pub/Sub topic
- Receives real-time stock data messages (from Step 1)
- Writes them as raw JSON files to a Cloud Storage bucket, organized by stock symbol and timestamp

## Requirements

- Cloud Storage	: To store the raw JSON stock data
- Cloud Functions	: To subscribe to Pub/Sub and write to GCS
- Pub/Sub	: The same topic used in Step 1 (stock-data-topic)
- Python SDKs	: `google-cloud-storage`, `json`, `base64`

## 


