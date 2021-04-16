import os
from random import randint
from slack_sdk import WebClient
from datetime import datetime
from bottoken import bot_token
from settings import channel_id
from greetings import Greetings
import ssl

def post_message():
    weekday = datetime.now().isoweekday()
    if 0 < weekday < 6:
        lucky_number = randint(1,6)
        if lucky_number % 2 == 0:
            greeting = Greetings().get_greeting()
            ssl._create_default_https_context = ssl._create_stdlib_context
            client = WebClient(token=bot_token)
            client.chat_postMessage(
                channel=channel_id,
                text=greeting
            )


post_message()
