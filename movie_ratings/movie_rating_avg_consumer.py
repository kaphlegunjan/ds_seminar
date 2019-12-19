from kafka import KafkaConsumer
from datetime import datetime
import json


consumer = KafkaConsumer(
    'MOVIE_RATING_AVG',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group6'
)


for message in consumer:
    rating_msg = json.loads(message.value)
    rating_timestamp = message.timestamp
    print("{} has a average rating of {} at {}".format(
        rating_msg['NAME'],
        rating_msg['AVG_RATING'],
        datetime.fromtimestamp(rating_timestamp/1000).strftime('%c'))
    )
