from telethon import TelegramClient
import sys

API_ID = 18917792
API_HASH = "1f1addf94481ee8ae1594ddc6ea78dfa"
BOT_TOKEN = "5567035354:AAEzENilm6ToojFZdZuErdtP8hryvRHTVZI"
LOG_GROUP = "MyLogAccManagerGroup"
ADMIN_ID = 5250298585

print("• Starting Bot . . .")

try:
    bot = TelegramClient(
        session="AccManager",
        api_id=API_ID,
        api_hash=API_HASH,
    ).start(bot_token=BOT_TOKEN)
except Exception as e:
    print(f"• Error On Create Bot: {e}")
    sys.exit()
