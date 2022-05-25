from bomber import bot
from telethon import events

@bot.on(events.NewMessage(pattern="(?i)\/start"))
async def start(event):
    await event.reply("**• Hello There!**")
