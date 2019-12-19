import os


class Config:

    TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
    TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET')
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    TWITTER_TOKEN_SECRET = os.environ.get('TWITTER_TOKEN_SECRET')

    SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')

    KAFKA_BOOTSTRAP_CONFIG = 'localhost:9092'
    KAFKA_MAIN_TOPIC = 'tweet_real_three'
