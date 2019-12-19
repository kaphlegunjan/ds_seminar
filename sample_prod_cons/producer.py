from kafka import KafkaProducer

import json
import uuid
import random


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


while True:
    new_id = str(uuid.uuid4())
    price = random.randint(50, 10000)
    payload = {
        "order_id": new_id,
        "price": price
    }
    str_payload = json.dumps(payload)
    producer.send(topic='orders', key=bytes(new_id, 'utf-8'),
                  value=bytes(str_payload, 'utf-8'))
