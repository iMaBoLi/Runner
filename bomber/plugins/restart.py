from bomber import bot
from telethon import events
import os

@Cmd(pattern="(?i)^\/restart$", admin_only=True)
async def restart(event):
    await event.reply("**• Bomber Restarted!**")
    os.system("bash start")
