from random import randrange
from kafka import KafkaProducer

import json
import time


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
movieIds = ['1', '2', '3', '4']

while True:
    rating = randrange(6, 11)
    movie = randrange(4)

    rating_payload = {
        'movieId': movieIds[movie],
        'rating': rating
    }

    str_data = json.dumps(rating_payload)
    producer.send(topic='ratings',
                  key=bytes(str(rating_payload['movieId']), 'utf-8'),
                  value=bytes(str_data, 'utf-8'))
    time.sleep(1)
