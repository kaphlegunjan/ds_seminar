from slackclient import SlackClient

from config import Config


def slack_message(message):
    token = Config.SLACK_API_TOKEN
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel='gunjan-alerting',
                text=message, username='Bot user',
                icon_emoji=':robot_face:')
