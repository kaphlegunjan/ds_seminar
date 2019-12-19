import tweepy as tw
import json

from config import Config
from kafka import KafkaProducer
import time


auth = tw.OAuthHandler(Config.TWITTER_API_KEY, Config.TWITTER_API_SECRET)
auth.set_access_token(Config.TWITTER_ACCESS_TOKEN, Config.TWITTER_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

hashtag = "therealreal"
date_since = "2018-01-01"

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

tweets = tw.Cursor(api.search,
                   q=hashtag,
                   lang='en',
                   since=date_since).items(5000)
count = 0
for tweet in tweets:
    count += 1
    data = tweet._json
    transformed_data = {
        'tweet_id': data['id'],
        'user_name': data['user']['name'],
        'verified': data['user']['verified'],
        'tweet': data['text'],
        'favorite_count': data['favorite_count']
    }

    str_data = json.dumps(data)
    producer.send(topic=Config.KAFKA_MAIN_TOPIC,
                  key=bytes(str(data['id']), 'utf-8'),
                  value=bytes(str_data, 'utf-8'))
    time.sleep(0.1)

print("Total loaded: {}".format(count))
