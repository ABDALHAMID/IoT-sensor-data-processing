import json
import time
import requests
from kafka import KafkaProducer
from dotenv import load_dotenv
import os

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "iot-sensor-data")
DATA_API_URL = os.getenv("DATA_API_URL", "http://simulator:5001/machines")  # internal Docker network

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_data():
    try:
        response = requests.get(DATA_API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data:", response.status_code)
            return []
    except Exception as e:
        print("Error fetching data:", e)
        return []

def produce_messages():
    data = fetch_data()
    for item in data:
        producer.send(KAFKA_TOPIC, item)
        print(f"Sent: {item}")
        time.sleep(1)  # simulate streaming

if __name__ == "__main__":
    while True:
        produce_messages()
        time.sleep(5)  # re-fetch new batch every 5 seconds
