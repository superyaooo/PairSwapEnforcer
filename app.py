import os
from slack_sdk import WebClient
from datetime import datetime
from bottoken import bot_token
from settings import channel_id
from greetings import Greetings

def post_message():
    weekday = datetime.now().isoweekday()
    if 0 < weekday < 6:
        client = WebClient(token=bot_token)
        # roll dice to decided whether to post message or not
        # get random greetings
        client.chat_postMessage()