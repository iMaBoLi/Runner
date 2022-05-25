from bomber import bot
from telethon import events
import os

@bot.on(events.NewMessage(pattern="(?i)\/restart"))
async def start(event):
    await event.reply("**• Bomber Restarted!**")
    os.system("bash start")
