import json
import os
import tempfile
from google.cloud import storage, bigquery

BUCKET_NAME = "stock-raw-data-stock-market-analytics-457419"
BQ_DATASET = "stock_data"
FLAT_FOLDER_SUFFIX = "_flat"

def flatten_alpha_vantage_json(symbol, raw_json):
    rows = []
    time_series = raw_json.get("data", {}).get("Time Series (5min)", {})
    for timestamp, values in time_series.items():
        rows.append({
            "symbol": symbol,
            "timestamp": timestamp,
            "open": values.get("1. open"),
            "high": values.get("2. high"),
            "low": values.get("3. low"),
            "close": values.get("4. close"),
            "volume": values.get("5. volume")
        })
    return rows

def main(event, context):
    file_path = event["name"]
    if not file_path.endswith(".json") or FLAT_FOLDER_SUFFIX in file_path:
        return  # Skip if not a raw .json or already processed

    symbol = file_path.split("/")[0]  # folder = symbol
    flat_blob_name = file_path.replace(symbol, f"{symbol}{FLAT_FOLDER_SUFFIX}")

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_path)

    try:
        content = blob.download_as_text()
        raw_json = json.loads(content)
        rows = flatten_alpha_vantage_json(symbol, raw_json)

        # Write to a temp file in NDJSON format
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmpfile:
            for row in rows:
                json.dump(row, tmpfile)
                tmpfile.write("\n")
            tmpfile_path = tmpfile.name

        # Upload flattened file to GCS
        flat_blob = bucket.blob(flat_blob_name)
        flat_blob.upload_from_filename(tmpfile_path)
        print(f"Flattened and uploaded: {flat_blob_name}")

        # Load into BigQuery
        bq_client = bigquery.Client()
        table_id = f"{bq_client.project}.{BQ_DATASET}.{symbol.lower()}_flat"

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect=True,
            write_disposition="WRITE_APPEND",
        )

        uri = f"gs://{BUCKET_NAME}/{flat_blob_name}"
        load_job = bq_client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()
        print(f"Loaded into BigQuery: {table_id}")
        os.remove(tmpfile_path)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
