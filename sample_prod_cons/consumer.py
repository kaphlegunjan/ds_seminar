from kafka import KafkaConsumer
import json
from datetime import datetime


consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sample-group'
)


for message in consumer:
    order_payload = json.loads(message.value)
    rating_timestamp = message.timestamp
    print("Order ID: {} sold at {} for {}".format(
        order_payload['order_id'],
        order_payload['price'],
        datetime.fromtimestamp(rating_timestamp/1000).strftime('%c'))
    )