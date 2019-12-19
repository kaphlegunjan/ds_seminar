from kafka import KafkaProducer

import json
import time


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

movies = [
    {
        'movieId': '1',
        'name': 'Home Alone 1',
        'year': 1990,
        'isChristmasMovie': True
    },
    {
        'movieId': '2',
        'name': 'Die Hard',
        'year': 2001,
        'isChristmasMovie': False
    },
    {
        'movieId': '3',
        'name': 'Home Alone 2',
        'year': 1995,
        'isChristmasMovie': True
    },
    {
        'movieId': '4',
        'name': 'Joker',
        'year': 2020,
        'isChristmasMovie': False
    }
]

for movie in movies:
    str_data = json.dumps(movie)
    producer.send(topic='movie', key=bytes(str(movie['movieId']), 'utf-8'),
                  value=bytes(str_data, 'utf-8'))
    time.sleep(1)