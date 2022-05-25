from telethon import TelegramClient
from decouple import config
import sys

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
ADMIN_ID = config("ADMIN_ID", default=None, cast=int)

print("• Starting Bot . . .")

try:
    bot = TelegramClient(
        session="Bomber",
        api_id=API_ID,
        api_hash=API_HASH,
    ).start(bot_token=BOT_TOKEN)
except Exception as e:
    print(f"• Error On Create Bot: {e}")
    sys.exit()
