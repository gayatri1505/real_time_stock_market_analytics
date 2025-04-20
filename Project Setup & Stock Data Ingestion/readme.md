# Goal

- Create a Cloud Function on Google Cloud that:
  - Fetches real-time stock prices using the Alpha Vantage API
  - Publishes the data to a Pub/Sub topic
  - Runs every 5 minutes via Cloud Scheduler

## Requirements

- Cloud Provider : Google Cloud Platform
- API Used: Alpha Vantage
- Language: Python 3.10
- GCP Services: Cloud Functions, Pub/Sub, Cloud Scheduler
- Python Libraries: requests, google-cloud-pubsub

## GCP Setup

1. **Create GCP Project** :
   - Create a project from the GCP Console
   - Example name: `stock-market-analytics`

2. **Enable Required APIs** :
   - Cloud Functions
   - Cloud Pub/Sub
   - Cloud Scheduler
   - BigQuery
   - Cloud Storage

3. **Create Pub/Sub Topic** :
   `gcloud pubsub topics create stock-data-topic`

4. **Create a folder** :
   - Add `main.py` and `requirements.txt` files.
   - Replace:
      - "YOUR_ALPHA_VANTAGE_API_KEY" with your actual API key
      - "your-gcp-project-id" with your GCP project ID

## Deploy Cloud Function

 `gcloud functions deploy fetch_stock_data \` \
  `--runtime python310 \` \
  `--trigger-topic stock-data-topic \` \
 ` --source . \` \
 ` --entry-point main \` \
  `--region us-central1`

## Fix IAM Role Binding for Cloud Build

  1. Get your project number :
     `gcloud projects describe project_id --format="value(projectNumber)"`

  2.  Grant the IAM role:
     `gcloud projects add-iam-policy-binding stock-market-analytics-457419 \` \
  `--member="serviceAccount:YOUR_PROJECT_NUMBER@cloudbuild.gserviceaccount.com" \` \
  `--role="roles/editor"`

## Schedule Cloud function (Every 5 mins)
Use Cloud Scheduler to trigger the function via Pub/Sub.

`gcloud scheduler jobs create pubsub trigger-stock-fetch \`\
  `--schedule="*/5 * * * *" \`\
  `--topic=stock-data-topic \`\
  `--message-body="{}" \`\
  `--time-zone="America/New_York" \`\
  `--location=us-central1`

## Output
- Function fetch_stock_data is ACTIVE
- Publishes stock data to Pub/Sub every 5 minutes
