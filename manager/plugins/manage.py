from manager import bot, LOG_GROUP
from telethon import TelegramClient, events
from manager.functions import delete_file
import re

@bot.on(events.CallbackQuery(data=re.compile("logout\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    

@bot.on(events.CallbackQuery(data=re.compile("getcodes\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))


@bot.on(events.CallbackQuery(data=re.compile("resetauthorization\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
