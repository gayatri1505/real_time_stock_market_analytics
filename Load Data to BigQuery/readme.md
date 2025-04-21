In this step, we created an automated pipeline that listens for new files in Google Cloud Storage (GCS), flattens Alpha Vantage JSON data, and loads it into BigQuery. This enables real-time analytics on structured stock data.

# Goal

- Detect new JSON files in GCS.
- Flatten the nested Alpha Vantage time series data.
- Store the flattened data as newline-delimited JSON.
- Automatically load it into BigQuery.



