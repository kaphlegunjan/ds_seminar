from kafka import KafkaConsumer
import json
from twitter_demo import slack_integration as si


consumer = KafkaConsumer(
    'VERIFIED_TWEETS',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='tweet-group4'
)


for message in consumer:
    content = json.loads(message.value)
    tweet = content['TWEET']
    handle = content['HANDLE']
    status_id = content['STATUS_ID']
    tweet_link = "www.twitter.com/statuses/{}".format(status_id)
    msg = "@{} just tweeted: {}.\n Link: {}".format(handle, tweet, tweet_link)
    si.slack_message(msg)
