# Goal
- Listens to the stock-data-topic Pub/Sub topic
- Receives real-time stock data messages (from Step 1)
- Writes them as raw JSON files to a Cloud Storage bucket, organized by stock symbol and timestamp

## Requirements

- Cloud Storage	: To store the raw JSON stock data
- Cloud Functions	: To subscribe to Pub/Sub and write to GCS
- Pub/Sub	: The same topic used in Step 1 (stock-data-topic)
- Python SDKs	: `google-cloud-storage`, `json`, `base64`

## Step-by-Step Workflow

1. **Create a Google Cloud Storage Bucket** 
   
   `export PROJECT_ID=$(/full/path/to/gcloud config get-value project)` \
   `export BUCKET_NAME="stock-raw-data-$PROJECT_ID"` \
   `/full/path/to/gsutil mb -l us-central1 gs://$BUCKET_NAME` \
    (Make sure to replace /full/path/to/ with your actual Google Cloud SDK path)

2. **Create Deployment Folder**
   
   `mkdir pubsub-to-gcs` \
   `cd pubsub-to-gcs` \
   Add main.py and requirements.txt 

3. **Deploy Cloud Function**

   `/path/to/gcloud functions deploy pubsub_to_gcs \` \
  `--runtime python310 \` \
  `--trigger-topic stock-data-topic \` \
  `--source . \` \
  `--entry-point main \` \
  `--region us-central1 `

4. **Trigger the Pipeline Manually (Optional)**

   `../google-cloud-sdk/bin/gcloud scheduler jobs run trigger-stock-fetch --location=us-central1`

  This will:
    - Trigger fetch_stock_data (Step 1)
    - Which publishes messages to Pub/Sub
    - Which triggers pubsub_to_gcs (this function)
    - And writes JSON files to your GCS bucket

5. **Check Your Bucket**
   
   `../google-cloud-sdk/bin/gsutil ls gs://$BUCKET_NAME/`


## Output

Raw stock JSON files are now archived in Google Cloud Storage




