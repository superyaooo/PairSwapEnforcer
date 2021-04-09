# test.py
from slack_sdk import WebClient
import logging
import sys
# Load the local source directly
sys.path.insert(1, "env/lib/slack-sdk")
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
client = WebClient()
api_response = client.api_test()
