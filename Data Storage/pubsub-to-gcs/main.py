import base64
import json
from datetime import datetime
from google.cloud import storage

BUCKET_NAME = "stock-raw-data-stock-market-analytics-457419"  # ← replace with your real bucket name

def write_to_gcs(symbol, data):
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    blob_name = f"{symbol}/{timestamp}.json"

    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data), content_type="application/json")
    print(f"Uploaded {blob_name}")

def main(event, context):
    if 'data' in event:
        decoded = base64.b64decode(event['data']).decode('utf-8')
        print("RAW MESSAGE:", decoded)  # ← Add this line
        payload = json.loads(decoded)
        symbol = payload.get("symbol", "unknown")
        write_to_gcs(symbol, payload)

