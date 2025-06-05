import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.environ['TG_API_ID'])
api_hash = os.environ['TG_API_HASH']

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string:", client.session.save())
