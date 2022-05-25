from bomber import bot
from telethon import events
from bomber.database import DB

@Cmd(pattern="(?i)^\/cleardb$")
async def cleardb(event):
    DB.flushall()
    await event.reply("**• Bomber Database Cleared!**")
