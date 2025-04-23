# Real-Time Stock Market Data Pipeline with Google Cloud & BigQuery

This project builds a **real-time stock data pipeline** using **Google Cloud Platform**, transforming and storing data from the Alpha Vantage API and enabling SQL-based analytics in BigQuery. It follows a modular architecture with ingestion, transformation, storage and analysis layers.

## Architecture Overview

Designed data engineering pipeline architecture using **Visio**.

![image](https://github.com/user-attachments/assets/f7ac3c2f-6fd3-4bdf-b21c-83fd5edb49cd)


## Tech Stack

| Layer             | Tool                        |
|------------------|-----------------------------|
| API Source        | Alpha Vantage API           |
| Scheduler         | Google Cloud Scheduler      |
| Messaging         | Google Pub/Sub              |
| Ingestion         | Google Cloud Functions      |
| Storage           | Google Cloud Storage        |
| Data Warehouse    | Google BigQuery             |
| Analysis          | BigQuery SQL, Colab         |
| Programming Scripts & Deployment | Python 3.10  |

## Data Flow Description

1. **API Triggering**:
   - Cloud Scheduler runs every 5 mins.
   - Publishes message to Pub/Sub topic.

2. **Raw Ingestion**:
   - `fetch_stock_data` Cloud Function fetches data and sends to Pub/Sub.
   - `pubsub_to_gcs` function stores raw JSON in Cloud Storage.

3. **Transformation & Cleaning**:
   - Another Cloud Function `flatten_and_load` flattens JSON structure and saves clean JSON to a separate bucket path.

4. **Load to BigQuery**:
   - Clean JSONs are ingested as typed tables in BigQuery (curated zone).

5. **Analysis & Dashboarding**:
   - SQL queries executed in BigQuery and Google Colab to explore patterns.


## Storage Zones
| Zone          | Description                                |
|---------------|--------------------------------------------|
| Raw Zone      | Stores raw API JSONs                       |
| Clean Zone    | Flattened structured JSONs                 |
| Curated Zone  | Analytical tables for SQL-based analysis   |


## SQL Analysis

Used BigQuery to perform a variety of stock data analyses:
- **Avg close per day**: Track how stocks behave daily
- **Price volatility**: `high - low` per timestamp
- **Avg volume**: Understand trading activity
- **Percent return**: Simulate gains/losses
- **Big price move with low volume**: Detect unusual trading behavior
- **Hourly pattern detection**: Volatility by hour
- **Open vs Close comparison**: Market reaction during trading hours

## Key Insights Highlight

| Insight Type                        | Observation                                                                 |
|------------------------------------|------------------------------------------------------------------------------|
| Highest Avg Volume                 | NVDA showed the highest average trading volume                              |
| Steadiest Performer                | MSFT had the least fluctuation among tech stocks                            |
| Largest Market Close Drop (17th)  | GOOGL showed a -0.92% drop despite mid-day gains                            |
| Market Open Surge Pattern         | Most stocks saw a spike between 12–16 UTC                                   |
| Anomalous Movement Detected        | Low-volume price swings in AAPL and AMZN                                    |

## Setup Instructions

Project is organized in four logical stages (FOLDERS). Follow this sequence when setting up:

1. Project Setup & Stock Data Ingestion
   
   Configure and trigger data ingestion from the Alpha Vantage API.

2. Data Storage
   
   Store data in Google Cloud Storage

3. Load Data to BigQuery
   
   Move clean data into structured tables in BigQuery.

4. Analytics
   
   Perform SQL-based analysis and visualizations.

   
   



