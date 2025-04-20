
#To make HTTP requests in Python.
import requests
import json
#pubsub_v1 is the client library for Pub/Sub — a messaging service by Google Cloud. 
#It lets you publish messages to topics or subscribe to them.
from google.cloud import pubsub_v1

API_KEY = "YOUR_API_KEY"
STOCKS = ['AAPL','MSFT','NVDA','AMZN','GOOGL']
PROJECT_ID = "YOUR_PROJECT_ID"
TOPIC_ID = "stock-data-topic"


publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

def publish_to_pubsub(data):
    payload = json.dumps(data).encode("utf-8")
    future = publisher.publish(topic_path, payload)
    print(f"Published message ID: {future.result()}")

def main(event, context):
    for symbol in STOCKS:
        data = get_stock_data(symbol)
        publish_to_pubsub({
            "symbol": symbol,
            "data": data
        })


