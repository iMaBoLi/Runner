from bomber import bot
from telethon import events
from bomber.database import DB

@bot.on(events.NewMessage(pattern="(?i)\/cleardb"))
async def start(event):
    DB.flushall()
    await event.reply("**• Bomber Database Cleared!**")
