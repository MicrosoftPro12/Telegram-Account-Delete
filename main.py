import random
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import SetAccountTTL, DeleteAccount
from telethon.tl.types import AccountDaysTTL

api_id = int(os.environ['TG_API_ID'])
api_hash = os.environ['TG_API_HASH']
session_str = os.environ['TG_SESSION']

should_delete = random.random() < 0.01  # 1%
if not should_delete:
    print("今天安全无事。")
    exit(0)

use_ttl_method = random.choice([True, False])

client = TelegramClient(StringSession(session_str), api_id, api_hash)

with client:
    if use_ttl_method:
        print("🎯中奖了，使用 `setAccountTTL(days=0)` 触发销号！")
        client(SetAccountTTL(AccountDaysTTL(days=0)))
    else:
        print("🎯中奖了，使用 `deleteAccount()` 触发销号！")
        client(DeleteAccount(reason="russian roulette"))
